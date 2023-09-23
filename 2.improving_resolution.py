import cv2
import argparse
# argparse: Library for parsing command-line arguments.

def parse_arguments() -> argparse.Namespace:
    parser= argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument(
        "--webcam_res",
        default=[1280,720],
        nargs=2,
        type=int
    )
    args =parser.parse_args()
    return args
    
    
    
def main():
    args = parse_arguments()
    frame_width ,frame_height = args.webcam_res
    
    cap=cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
    
    while True:
        ret,frame= cap.read()
        cv2.imshow("yolov8",frame)
        
        if(cv2.waitKey(30)==27):
            ## 27 is the ASCII value of esc button
            break
        
        
if __name__ == '__main__':
    main()
    
    
    