import os

pages = [
    "services.html",
    "portfolio.html",
    "gallery.html",
    "team.html",
    "blog.html",
    "contact.html",
    "careers.html",
    "faq.html",
    "residential-projects.html",
    "commercial-projects.html",
    "interior-design.html",
    "landscape-design.html",
    "urban-planning.html",
    "smart-homes.html",
    "project-details.html",
    "single-blog.html",
    "consultation-booking.html",
    "construction-management.html",
    "sustainability.html",
    "3d-visualization.html",
    "virtual-tour.html",
    "awards.html",
    "testimonials.html"
]

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | ARCHVISTA STUDIO</title>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Bootstrap Icons -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <!-- AOS Animation CSS -->
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    
    <!-- Custom CSS -->
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/animations.css">
    <link rel="stylesheet" href="css/responsive.css">
</head>
<body>

    <!-- Header / Navigation -->
    <header class="scrolled">
        <div class="container px-6 flex justify-between items-center h-full">
            <a href="index.html" class="logo-text text-navy">ARCHVISTA</a>
            
            <!-- Desktop Nav -->
            <nav class="desktop-nav hidden md:flex items-center">
                <a href="index.html" class="nav-link text-navy">Home</a>
                <a href="about.html" class="nav-link text-navy">About</a>
                <a href="services.html" class="nav-link text-navy">Services</a>
                <a href="portfolio.html" class="nav-link text-navy">Portfolio</a>
                <a href="blog.html" class="nav-link text-navy">Journal</a>
                <a href="contact.html" class="nav-link text-navy">Contact</a>
                <a href="consultation-booking.html" class="nav-link ml-8 btn-primary">Book Consultation</a>
            </nav>

            <!-- Mobile Menu Btn -->
            <button class="mobile-menu-btn hidden text-navy text-3xl focus:outline-none">
                <i class="bi bi-list"></i>
            </button>
        </div>
    </header>

    <!-- Menu Overlay -->
    <div class="menu-overlay"></div>

    <!-- Page Banner -->
    <section class="page-banner pt-32">
        <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80" alt="Banner" class="page-banner-bg">
        <div class="hero-overlay"></div>
        <div class="container px-6 relative z-10 text-center">
            <h1 class="page-banner-title reveal-text text-white">{title}</h1>
            <div class="breadcrumb" data-aos="fade-up" data-aos-delay="200">
                <a href="index.html">Home</a>
                <span>/</span>
                <span>{title}</span>
            </div>
        </div>
    </section>

    <!-- Main Content Placeholder -->
    <section class="py-24 bg-white min-h-[50vh] flex items-center justify-center">
        <div class="container px-6 text-center">
            <h2 class="section-title text-navy">{title} Content Coming Soon</h2>
            <p class="text-gray-500">This section is part of the extensive ARCHVISTA STUDIO experience.</p>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container px-6">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">
                <div>
                    <h2 class="text-2xl font-bold font-heading text-white mb-6 tracking-widest">ARCHVISTA</h2>
                    <p class="text-sm mb-6 pr-4">Designing tomorrow's landmarks today.</p>
                    <div class="flex">
                        <a href="#" class="social-icon"><i class="bi bi-instagram"></i></a>
                        <a href="#" class="social-icon"><i class="bi bi-linkedin"></i></a>
                    </div>
                </div>
                <div>
                    <h3 class="footer-title">Quick Links</h3>
                    <ul class="space-y-2">
                        <li><a href="about.html" class="footer-link">About Studio</a></li>
                        <li><a href="portfolio.html" class="footer-link">Our Projects</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom text-sm text-gray-500 mt-12 pt-6 border-t border-gray-800">
                <p>&copy; 2026 ARCHVISTA STUDIO. All Rights Reserved.</p>
            </div>
        </div>
    </footer>

    <!-- GSAP & AOS -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    
    <!-- Custom JS -->
    <script src="js/script.js"></script>
    <script src="js/animations.js"></script>

</body>
</html>
"""

def generate():
    for page in pages:
        if not os.path.exists(page):
            # Convert dash-case to Title Case for the title
            title = page.replace('.html', '').replace('-', ' ').title()
            content = template.format(title=title)
            with open(page, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Created {page}")

if __name__ == "__main__":
    generate()
