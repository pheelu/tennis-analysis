from utils import (read_video, 
                   save_video)

from trackers import PlayerTracker

def main():
    # Read video frames
    input_video_path = 'input_videos/input_video.mp4'
    video_frames = read_video(input_video_path)


    # Detect players in the video
    player_tracker = PlayerTracker('yolov8x.pt')
    player_detections = player_tracker.detect_frames(video_frames)

    # Draw bounding boxes around players
    ## Draw players bboxes
    output_video_frames = player_tracker.draw_bboxes(video_frames, player_detections)

    save_video(video_frames, 'output_videos/output_video.avi')

if __name__ == "__main__":
    main()