import os
import re
import urllib.request
import random

verified_ids = [
    "1600596542815-ffad4c1539a9",
    "1600607687920-4e20b33a8512",
    "1486406146926-c627a92ad1ab",
    "1512917774080-9991f1c4c750",
    "1600566753086-00f18fb6b3ea",
    "1618221118493-9cfa1a1c00aa",
    "1497366216548-37526070297c",
    "1503387762-592deb58ef4e",
    "1600585154340-be6161a56a0c",
    "1513694203232-719a280e022f",
    "1541888087519-92d137e96843",
    "1449844908441-8829872d2607",
    "1431538512261-2f04e14f86d6",
    "1464938050520-ef2270bb8ce8",
    "1486304873000-235cb1c5ed80",
    "1511818966892-d7d671fc27a1",
    "1600607688969-a5bfcd64bd28",
    "1600210491369-0df331005fbc",
    "1600210492486-724fe5c67fb0",
    "1600210492493-0946911123ea"
]

def ensure_images_exist():
    print("Downloading images locally to guarantee 100% visibility...")
    if not os.path.exists('images'):
        os.makedirs('images')
        
    for i, img_id in enumerate(verified_ids):
        filename = f"images/arch_{i+1}.jpg"
        if not os.path.exists(filename):
            url = f"https://images.unsplash.com/photo-{img_id}?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80"
            print(f"Downloading {filename}...")
            try:
                # Add a user-agent to avoid basic blocks
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as response, open(filename, 'wb') as out_file:
                    out_file.write(response.read())
            except Exception as e:
                print(f"Error downloading {filename}: {e}")

def replace_with_local():
    print("Updating HTML files to use local images...")
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # We also need to replace the randomuser API images just in case they fail
    # We will use some downloaded images for people too, or just leave randomuser.me alone. 
    # Usually randomuser.me doesn't fail. We will only fix unsplash.
    
    pattern = r'https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=\d+&q=80'
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        def repl(match):
            # Pick a random local image
            return f"images/arch_{random.randint(1, len(verified_ids))}.jpg"
            
        new_content = re.sub(pattern, repl, content)
        
        # In case there are some that missed the exact pattern match
        pattern2 = r'https://images\.unsplash\.com/[^\s"\'<>]+'
        def repl2(match):
            return f"images/arch_{random.randint(1, len(verified_ids))}.jpg"
            
        new_content = re.sub(pattern2, repl2, new_content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
    print("Done updating all HTML files.")

if __name__ == "__main__":
    ensure_images_exist()
    replace_with_local()
