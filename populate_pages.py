import os

# Content Blocks
header_html = """<!DOCTYPE html>
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
"""

footer_html = """
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

# Templates
template_services = """
    <section class="py-24 bg-white">
        <div class="container px-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center mb-16">
                <div>
                    <span class="section-subtitle">Overview</span>
                    <h2 class="section-title text-navy">Transforming Vision Into Reality</h2>
                    <p class="text-gray-600 mb-6">Our dedicated team approaches each project with a deep commitment to excellence, seamlessly integrating form and function.</p>
                    <ul class="space-y-4">
                        <li class="flex items-center text-gray-700"><i class="bi bi-check-circle-fill text-gold mr-3"></i> Innovative Conceptualization</li>
                        <li class="flex items-center text-gray-700"><i class="bi bi-check-circle-fill text-gold mr-3"></i> Sustainable Practices</li>
                        <li class="flex items-center text-gray-700"><i class="bi bi-check-circle-fill text-gold mr-3"></i> Expert Execution</li>
                    </ul>
                </div>
                <div class="reveal-image" data-aos="fade-left">
                    <img src="https://images.unsplash.com/photo-1600607687920-4e20b33a8512?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Service Image" class="w-full rounded-sm shadow-xl">
                </div>
            </div>
        </div>
    </section>
    
    <section class="py-20 bg-soft-gray">
        <div class="container px-6 text-center">
            <h2 class="text-3xl font-bold font-heading text-navy mb-8">Ready to start your project?</h2>
            <a href="consultation-booking.html" class="btn-primary">Book a Consultation</a>
        </div>
    </section>
"""

template_portfolio = """
    <section class="py-24 bg-white">
        <div class="container px-6">
            <div class="text-center mb-12">
                <span class="section-subtitle">Our Work</span>
                <h2 class="section-title text-navy">Discover Our {title}</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Project 1 -->
                <div class="project-card" data-aos="fade-up">
                    <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Project 1">
                    <div class="project-overlay">
                        <h3>Lumina Estate</h3>
                        <a href="project-details.html" class="text-gold text-sm font-bold uppercase mt-2">View Details</a>
                    </div>
                </div>
                <!-- Project 2 -->
                <div class="project-card" data-aos="fade-up" data-aos-delay="100">
                    <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Project 2">
                    <div class="project-overlay">
                        <h3>Nexus Tower</h3>
                        <a href="project-details.html" class="text-gold text-sm font-bold uppercase mt-2">View Details</a>
                    </div>
                </div>
                <!-- Project 3 -->
                <div class="project-card" data-aos="fade-up" data-aos-delay="200">
                    <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Project 3">
                    <div class="project-overlay">
                        <h3>Aura Penthouse</h3>
                        <a href="project-details.html" class="text-gold text-sm font-bold uppercase mt-2">View Details</a>
                    </div>
                </div>
                 <!-- Project 4 -->
                <div class="project-card" data-aos="fade-up" data-aos-delay="300">
                    <img src="https://images.unsplash.com/photo-1600607688969-a5bfcd64bd28?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Project 4">
                    <div class="project-overlay">
                        <h3>Zen Residence</h3>
                        <a href="project-details.html" class="text-gold text-sm font-bold uppercase mt-2">View Details</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

template_contact = """
    <section class="py-24 bg-white">
        <div class="container px-6">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16">
                <div>
                    <span class="section-subtitle">Get In Touch</span>
                    <h2 class="section-title text-navy">Let's Discuss Your Next Landmark</h2>
                    <p class="text-gray-600 mb-8">Reach out to our global headquarters or fill out the form below to begin a conversation with our lead architects.</p>
                    
                    <div class="flex items-start mb-6">
                        <i class="bi bi-geo-alt text-3xl text-gold mr-4"></i>
                        <div>
                            <h4 class="font-bold text-navy font-heading">Headquarters</h4>
                            <p class="text-gray-500 text-sm">124 Architecture Blvd, London, UK</p>
                        </div>
                    </div>
                    <div class="flex items-start mb-6">
                        <i class="bi bi-envelope text-3xl text-gold mr-4"></i>
                        <div>
                            <h4 class="font-bold text-navy font-heading">Email</h4>
                            <p class="text-gray-500 text-sm">hello@archvistastudio.com</p>
                        </div>
                    </div>
                    <div class="flex items-start mb-6">
                        <i class="bi bi-telephone text-3xl text-gold mr-4"></i>
                        <div>
                            <h4 class="font-bold text-navy font-heading">Phone</h4>
                            <p class="text-gray-500 text-sm">+44 20 7946 0958</p>
                        </div>
                    </div>
                </div>
                
                <div class="bg-soft-gray p-10 rounded-sm shadow-md" data-aos="fade-left">
                    <form>
                        <div class="mb-4">
                            <label class="block text-sm font-bold text-navy mb-2">Name</label>
                            <input type="text" required class="w-full p-3 border border-gray-300 rounded focus:outline-none focus:border-gold">
                        </div>
                        <div class="mb-4">
                            <label class="block text-sm font-bold text-navy mb-2">Email</label>
                            <input type="email" required class="w-full p-3 border border-gray-300 rounded focus:outline-none focus:border-gold">
                        </div>
                        <div class="mb-6">
                            <label class="block text-sm font-bold text-navy mb-2">Message</label>
                            <textarea rows="4" required class="w-full p-3 border border-gray-300 rounded focus:outline-none focus:border-gold"></textarea>
                        </div>
                        <button type="submit" class="btn-primary w-full">Send Message</button>
                    </form>
                </div>
            </div>
        </div>
    </section>
"""

template_team = """
    <section class="py-24 bg-white">
        <div class="container px-6">
            <div class="text-center mb-16">
                <span class="section-subtitle">Our Experts</span>
                <h2 class="section-title text-navy">The Visionaries</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Member 1 -->
                <div class="text-center group" data-aos="fade-up">
                    <div class="relative overflow-hidden mb-4 rounded-sm">
                        <img src="https://randomuser.me/api/portraits/women/44.jpg" alt="Elena Rostova" class="w-full h-80 object-cover grayscale group-hover:grayscale-0 transition-all duration-500">
                    </div>
                    <h3 class="text-xl font-bold font-heading text-navy">Elena Rostova</h3>
                    <p class="text-gold text-sm font-bold uppercase tracking-wider">Founder & Lead Architect</p>
                </div>
                <!-- Member 2 -->
                <div class="text-center group" data-aos="fade-up" data-aos-delay="100">
                    <div class="relative overflow-hidden mb-4 rounded-sm">
                        <img src="https://randomuser.me/api/portraits/men/32.jpg" alt="Marcus Vance" class="w-full h-80 object-cover grayscale group-hover:grayscale-0 transition-all duration-500">
                    </div>
                    <h3 class="text-xl font-bold font-heading text-navy">Marcus Vance</h3>
                    <p class="text-gold text-sm font-bold uppercase tracking-wider">Head of Urban Planning</p>
                </div>
                <!-- Member 3 -->
                <div class="text-center group" data-aos="fade-up" data-aos-delay="200">
                    <div class="relative overflow-hidden mb-4 rounded-sm">
                        <img src="https://randomuser.me/api/portraits/women/68.jpg" alt="Sarah Jenkins" class="w-full h-80 object-cover grayscale group-hover:grayscale-0 transition-all duration-500">
                    </div>
                    <h3 class="text-xl font-bold font-heading text-navy">Sarah Jenkins</h3>
                    <p class="text-gold text-sm font-bold uppercase tracking-wider">Lead Interior Designer</p>
                </div>
            </div>
        </div>
    </section>
"""

template_blog = """
    <section class="py-24 bg-white">
        <div class="container px-6">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Post 1 -->
                <article class="group" data-aos="fade-up">
                    <div class="relative overflow-hidden mb-6 rounded-sm">
                        <img src="https://images.unsplash.com/photo-1513694203232-719a280e022f?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Blog" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-700">
                    </div>
                    <h3 class="text-xl font-bold text-navy mb-3 font-heading"><a href="single-blog.html">Sustainable Architecture Trends 2026</a></h3>
                    <p class="text-gray-600 text-sm">Discover how new materials are changing the landscape of sustainable buildings.</p>
                </article>
                <!-- Post 2 -->
                <article class="group" data-aos="fade-up" data-aos-delay="100">
                    <div class="relative overflow-hidden mb-6 rounded-sm">
                        <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Blog" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-700">
                    </div>
                    <h3 class="text-xl font-bold text-navy mb-3 font-heading"><a href="single-blog.html">Minimalist Interior Masterclass</a></h3>
                    <p class="text-gray-600 text-sm">Less is more: A deep dive into creating space and serenity in urban homes.</p>
                </article>
                <!-- Post 3 -->
                <article class="group" data-aos="fade-up" data-aos-delay="200">
                    <div class="relative overflow-hidden mb-6 rounded-sm">
                        <img src="https://images.unsplash.com/photo-1541888087519-92d137e96843?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Blog" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-700">
                    </div>
                    <h3 class="text-xl font-bold text-navy mb-3 font-heading"><a href="single-blog.html">The Rebirth of Brutalism</a></h3>
                    <p class="text-gray-600 text-sm">Why concrete structures are making a huge comeback in modern city scapes.</p>
                </article>
            </div>
        </div>
    </section>
"""

template_generic = """
    <section class="py-24 bg-white">
        <div class="container px-6 max-w-4xl text-center">
            <h2 class="section-title text-navy">{title} Information</h2>
            <p class="text-gray-600 leading-relaxed text-lg mb-8">
                At ARCHVISTA STUDIO, we dedicate our expertise to providing comprehensive details and services regarding {title}. Our approach ensures luxury, sustainability, and structural integrity across every phase of the project lifecycle.
            </p>
            <p class="text-gray-600 leading-relaxed text-lg mb-8">
                Explore our innovative methodologies and discover how our award-winning team seamlessly blends artistic vision with technical precision to deliver outstanding results that redefine modern living and working spaces.
            </p>
            <a href="contact.html" class="btn-primary">Speak to an Expert</a>
        </div>
    </section>
"""

pages_mapping = {
    "services.html": template_services,
    "interior-design.html": template_services,
    "landscape-design.html": template_services,
    "urban-planning.html": template_services,
    "smart-homes.html": template_services,
    "construction-management.html": template_services,
    "sustainability.html": template_services,
    "3d-visualization.html": template_services,
    
    "portfolio.html": template_portfolio,
    "gallery.html": template_portfolio,
    "residential-projects.html": template_portfolio,
    "commercial-projects.html": template_portfolio,
    "project-details.html": template_portfolio,
    
    "contact.html": template_contact,
    "consultation-booking.html": template_contact,
    
    "team.html": template_team,
    "awards.html": template_team,
    "careers.html": template_team,
    
    "blog.html": template_blog,
    "single-blog.html": template_blog,
    
    "testimonials.html": template_generic,
    "faq.html": template_generic,
    "virtual-tour.html": template_generic
}

for page, content_template in pages_mapping.items():
    if os.path.exists(page):
        title = page.replace('.html', '').replace('-', ' ').title()
        full_content = header_html.format(title=title) + content_template.format(title=title) + footer_html
        with open(page, 'w', encoding='utf-8') as f:
            f.write(full_content)
        print(f"Populated {page}")
