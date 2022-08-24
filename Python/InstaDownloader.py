import instaloader
ig = instaloader . Instaloader()
dp = input("Wanted User: ")
ig.download_profile(dp, profile_pic_only=True)