import zbar

from PIL import Image
import cv2
import purchase_parser


def read_qrcode(capture):

   # Breaks down the video into frames
   ret, frame = capture.read()

   # Displays the current frame
   cv2.imshow('Current', frame)

   # Converts image to grayscale.
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   # Uses PIL to convert the grayscale image into a ndary array that ZBar can understand.
   image = Image.fromarray(gray)
   width, height = image.size
   zbar_image = zbar.Image(width, height, 'Y800', image.tobytes())

   # Scans the zbar image.
   scanner = zbar.ImageScanner()
   scanner.scan(zbar_image)

   ret_data = ""
   ret_stat = 0
   # Prints data from image.
   for decoded in zbar_image:
      # print(decoded.data)
      ret_data = decoded.data 
      ret_stat = 1

   return ret_data, ret_stat

def continue_question():

   while(1):

      # For python3 input()
      decision = raw_input("Successful processed. Continue? Y/N: ")
      
      if decision == 'Y' or decision == 'y':
         return True
      elif decision == 'N' or decision == 'n':
         return False


def main():
   """
   A simple function that captures webcam video utilizing OpenCV. The video is then broken down into frames which
   are constantly displayed. The frame is then converted to grayscale for better contrast. Afterwards, the image
   is transformed into a numpy array using PIL. This is needed to create zbar image. This zbar image is then scanned
   utilizing zbar's image scanner and will then print the decodeed message of any QR or bar code. To quit the program,
   press "q".
   :return:
   """

   # Begin capturing video. You can modify what video source to use with VideoCapture's argument. It's currently set
   # to be your webcam.
   capture = cv2.VideoCapture(0)
   counter = 0;
   while True:
      qr_data, ret_stat = read_qrcode(capture)

      if ret_stat:
         counter = counter + 1
         print(counter)
         try:
            status = purchase_parser.parse_data(qr_data)
         except:
            print('Error: Parsing exception\n')

         if(status):
            if continue_question() == False:
               break

      try:
         # To quit this program press q.
         if cv2.waitKey(1) & 0xFF == ord('q'):
            break
      except:
         print('Exception in waitKey()')
        

if __name__ == "__main__":
   main()
