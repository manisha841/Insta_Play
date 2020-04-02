import instaloader as insta
profile=insta.Instaloader()
a=input("Enter the username:")
profile.download_profile(a,profile_pic_only=True)
#profile.download_profile(a,profile_pic=true)

profile.download_profile(a,download_tagged_only=True)
profile.download_saved_posts(a,download_saved_posts=True)
profile.download_videos(a,download_videos=True)
profile.download_profile(a,download_stories_only=True)
