import os
import random
import re

# Verified working Unsplash image IDs for architecture / interior
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

def get_random_image(width=800):
    img_id = random.choice(verified_ids)
    return f"https://images.unsplash.com/photo-{img_id}?ixlib=rb-4.0.3&auto=format&fit=crop&w={width}&q=80"

gallery_html_template = """
    <!-- Extended Image Gallery -->
    <section class="py-16 bg-white">
        <div class="container px-6">
            <div class="text-center mb-10">
                <span class="section-subtitle">Visuals</span>
                <h2 class="section-title text-navy">Project Gallery</h2>
            </div>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                <div class="reveal-image" data-aos="fade-up" data-aos-delay="0"><img src="{img1}" class="w-full h-48 object-cover rounded shadow-sm hover:scale-105 transition-transform cursor-pointer lightbox-trigger"></div>
                <div class="reveal-image" data-aos="fade-up" data-aos-delay="100"><img src="{img2}" class="w-full h-48 object-cover rounded shadow-sm hover:scale-105 transition-transform cursor-pointer lightbox-trigger"></div>
                <div class="reveal-image" data-aos="fade-up" data-aos-delay="200"><img src="{img3}" class="w-full h-48 object-cover rounded shadow-sm hover:scale-105 transition-transform cursor-pointer lightbox-trigger"></div>
                <div class="reveal-image" data-aos="fade-up" data-aos-delay="300"><img src="{img4}" class="w-full h-48 object-cover rounded shadow-sm hover:scale-105 transition-transform cursor-pointer lightbox-trigger"></div>
                <div class="reveal-image" data-aos="fade-up" data-aos-delay="400"><img src="{img5}" class="w-full h-48 object-cover rounded shadow-sm hover:scale-105 transition-transform cursor-pointer lightbox-trigger"></div>
                <div class="reveal-image" data-aos="fade-up" data-aos-delay="500"><img src="{img6}" class="w-full h-48 object-cover rounded shadow-sm hover:scale-105 transition-transform cursor-pointer lightbox-trigger"></div>
                <div class="reveal-image" data-aos="fade-up" data-aos-delay="600"><img src="{img7}" class="w-full h-48 object-cover rounded shadow-sm hover:scale-105 transition-transform cursor-pointer lightbox-trigger"></div>
                <div class="reveal-image" data-aos="fade-up" data-aos-delay="700"><img src="{img8}" class="w-full h-48 object-cover rounded shadow-sm hover:scale-105 transition-transform cursor-pointer lightbox-trigger"></div>
            </div>
        </div>
    </section>
"""

def process_files():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # 1. Replace broken images with verified ones in ALL files
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to find all unsplash URLs
        pattern = r'https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+\?ixlib=rb-4\.0\.3&auto=format&fit=crop&w=\d+&q=80'
        
        def repl(match):
            width_match = re.search(r'w=(\d+)', match.group(0))
            width = width_match.group(1) if width_match else "800"
            return get_random_image(width)
            
        new_content = re.sub(pattern, repl, content)
        
        # Only add the extended gallery to specific files so it doesn't break index/contact layout
        if file not in ['index.html', 'contact.html']:
            if '<!-- Extended Image Gallery -->' not in new_content:
                gallery = gallery_html_template.format(
                    img1=get_random_image(600), img2=get_random_image(600),
                    img3=get_random_image(600), img4=get_random_image(600),
                    img5=get_random_image(600), img6=get_random_image(600),
                    img7=get_random_image(600), img8=get_random_image(600),
                )
                new_content = new_content.replace('<footer>', gallery + '\n    <footer>')

        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
    print("Fixed image links and added galleries to subpages.")

if __name__ == "__main__":
    process_files()
