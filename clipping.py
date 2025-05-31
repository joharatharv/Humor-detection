import os
import random
from moviepy.editor import VideoFileClip

def create_random_clips(video_path, num_clips=3, clip_duration=30):
    """
    Create random clips from a video file
    
    Args:
        video_path (str): Path to the input video file
        num_clips (int): Number of clips to create (default: 3)
        clip_duration (int): Duration of each clip in seconds (default: 30)
    """
    
    # Checking if video file exists
    if not os.path.exists(video_path):
        print(f"Error: Video file '{video_path}' not found!")
        return
    
    try:
        print("Loading video...")
        video = VideoFileClip(video_path)
        video_duration = video.duration
        
        print(f"Video duration: {video_duration:.2f} seconds")
        
        # Check if video is long enough for the clips
        if video_duration < clip_duration:
            print(f"Error: Video is too short! Need at least {clip_duration} seconds.")
            return
        
        # Calculate maximum start time for clips
        max_start_time = video_duration - clip_duration
        
        # Generate random start times
        start_times = []
        for i in range(num_clips):
            start_time = random.uniform(0, max_start_time)
            start_times.append(start_time)
        
        # Sort start times to avoid overlaps (optional)
        start_times.sort()
        
        # Create clips
        for i, start_time in enumerate(start_times, 1):
            end_time = start_time + clip_duration
            
            print(f"Creating clip {i}: {start_time:.2f}s - {end_time:.2f}s")
            
            # Extract the clip
            clip = video.subclip(start_time, end_time)
            
            # Generate output filename
            base_name = os.path.splitext(os.path.basename(video_path))[0]
            output_filename = f"{base_name}_clip_{i}_{int(start_time)}s.mp4"
            
            # Write the clip
            clip.write_videofile(
                output_filename,
                codec='libx264',
                audio_codec='aac',
                temp_audiofile='temp-audio.m4a',
                remove_temp=True,
                verbose=False,
                logger=None
            )
            
            print(f"Saved: {output_filename}")
            
            # Close the clip to free memory
            clip.close()
        
        # Close the original video
        video.close()
        print("All clips created successfully!")
        
    except Exception as e:
        print(f"Error processing video: {str(e)}")

# Main execution
if __name__ == "__main__":
    #video path
    video_file = "Ameeron ka Accent _ Crowdwork _ Stand up comedy by Rajat Chauhan (48th Video).mp4"
    
    # Create 3 random 30-second clips
    create_random_clips(video_file, num_clips=3, clip_duration=30)
    
    print("\nNote: Make sure your video file has the correct extension!")
    print("If you get a file not found error, try adding the extension like '.mp4'")
