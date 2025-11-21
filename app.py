import streamlit as st

# Page configuration
st.set_page_config(
    page_title="SoulShutter Photography Studio | Professional Portfolio",
    page_icon="📸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for polished, professional look with enhanced mobile responsiveness
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600;700&family=Cinzel:wght@400;500;600;700&display=swap');

    * {
        font-family: 'Inter', sans-serif;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body, .main, .stApp {
        background: #0a0a0a !important;
        color: #ebebeb;
        overflow-x: hidden;
    }

    /* Header and Sidebar hidden for a clean look */
    .stApp > header, .stSidebar {display: none;}
    .stApp > div {padding-top: 0 !important;}

    /* Navigation Bar - Mobile Optimized */
    .main-nav {
        position: fixed;
        top: 0; left: 0; right: 0;
        background: rgba(10, 10, 10, 0.98);
        backdrop-filter: blur(25px);
        z-index: 1200;
        padding: 20px 0;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        transition: all 0.3s ease;
    }
    .nav-content {
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 20px;
    }
    .nav-logo {
        font-family: 'Cinzel', serif;
        font-size: 1.4rem;
        color: #ffffff;
        letter-spacing: 0.25em;
        font-weight: 500;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    .nav-logo:hover {color: #cccccc;}
    .nav-links {display: flex; gap: 15px;}
    .nav-button {
        background: rgba(255,255,255,0.1);
        color: #ebebeb;
        border: 1px solid rgba(255,255,255,0.2);
        padding: 10px 18px;
        border-radius: 25px;
        text-decoration: none;
        font-size: 0.8rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        transition: all 0.3s ease;
        cursor: pointer;
        outline: none;
        white-space: nowrap;
    }
    .nav-button:hover, .nav-button:focus {
        background: rgba(255,255,255,0.15);
        border-color: rgba(255,255,255,0.3);
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }

/* Hero Section - Mobile Optimized */
.hero-section {
    background: linear-gradient(rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.55)),
                url('https://images.unsplash.com/photo-1516035069371-29a1b244cc32?q=80&w=464&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
    background-size: cover;
    background-position: center;
    background-attachment: scroll;
    padding: 150px 0 80px 0;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    position: relative;
    margin-top: -80px;
    text-align: center;
}

    .lens-flare {
        position: absolute; top: 20%; right: 15%;
        width: 200px; height: 200px;
        background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 70%);
        border-radius: 50%; filter: blur(25px);
        animation: rotate 25s linear infinite;
        opacity: 0.4;
        pointer-events: none;
    }
    .lens-flare-2 {
        position: absolute; top: 60%; left: 10%;
        width: 120px; height: 120px;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        border-radius: 50%; filter: blur(20px);
        animation: rotate 20s linear infinite reverse;
        opacity: 0.3;
        pointer-events: none;
    }
    @keyframes rotate {to{transform:rotate(360deg);}from{transform:rotate(0deg);}}

    .hero-content {
        position: relative; 
        z-index: 2; 
        max-width: 1200px; 
        margin: 0 auto; 
        padding: 0 20px;
        width: 100%;
    }
    .camera-icon {
        font-size: 4rem;
        margin-bottom: 30px;
        animation: float 6s ease-in-out infinite;
        filter: drop-shadow(0 0 30px rgba(255,255,255,0.4));
        display: inline-block;
    }
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        33% { transform: translateY(-15px) rotate(2deg); }
        66% { transform: translateY(-8px) rotate(-2deg); }
    }
    .hero-main-title {
        font-family: 'Cinzel', serif;
        font-size: 3.5rem;
        font-weight: 300;
        color: #fff;
        text-transform: uppercase;
        letter-spacing: 0.3em;
        margin-top: -10px;
        text-shadow: 0 0 40px rgba(255,255,255,0.6);
        position: relative;
        line-height: 1.1;
        word-wrap: break-word;
    }
    .hero-main-title::after{
        content:'';
        display:block;
        position: absolute;
        bottom: -20px;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 2px;
        background: linear-gradient(90deg, transparent, #ffffff, transparent);
        animation: widthPulse 3s ease-in-out infinite;
    }
    @keyframes widthPulse {
        0%, 100% { width: 100px; }
        50% { width: 130px; }
    }

    .hero-subtitle {
        font-family: 'Playfair Display', serif;
        font-size: 1.2rem;
        font-weight: 300; 
        color: #e0e0e0;
        letter-spacing: 0.3em;
        text-transform: uppercase;
        font-style: italic;
        margin-bottom: 3rem;
        line-height: 1.4;
        word-wrap: break-word;
    }
    .photography-badge {
        display: inline-flex;
        align-items: center;
        gap: 15px;
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(20px);
        padding: 15px 25px;
        border-radius: 50px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        margin-top: 30px;
        transition: all 0.3s ease;
        flex-wrap: wrap;
        justify-content: center;
    }
    .photography-badge:hover {
        background: rgba(255, 255, 255, 0.12);
        border-color: rgba(255, 255, 255, 0.25);
        transform: translateY(-2px);
    }
    .badge-icon {font-size: 1.4rem; filter: drop-shadow(0 0 10px rgba(255,255,255,0.3));}
    .badge-text {
        font-family: 'Inter', sans-serif;
        font-size: 0.9rem;
        letter-spacing: 0.15em;
        color: #fff;
        text-transform: uppercase;
        font-weight: 400;
        text-align: center;
    }
    .scroll-indicator {
        position: absolute;
        bottom: 40px;
        left: 50%;
        transform: translateX(-50%);
        color: #cccccc;
        text-transform: uppercase;
        font-size: 0.8rem;
        letter-spacing: 0.2em;
        animation: bounce 2s infinite;
        font-weight: 400;
    }
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateX(-50%) translateY(0); }
        40% { transform: translateX(-50%) translateY(-10px); }
        60% { transform: translateX(-50%) translateY(-5px); }
    }

    .section-anchor {position: relative; top: -80px; visibility: hidden;}

    /* Portfolio Gallery - Mobile Optimized */
    .gallery-section {
        max-width: 1400px;
        margin: 0 auto;
        padding: 60px 15px 0 15px;
    }
    .gallery-card {
        margin: 80px 0;
        position: relative;
        overflow: hidden;
        border-radius: 2px;
        transition: box-shadow 0.3s;
        cursor: pointer;
    }
    .gallery-card:hover {
        box-shadow: 0 7px 88px -25px rgba(254,217,183,0.3);
    }
    .card-image-wrapper {
        position: relative;
        overflow: hidden;
        height: 70vh;
        min-height: 500px;
    }
    .card-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 1.4s cubic-bezier(.23,1,.32,1), filter 1.4s cubic-bezier(.23,1,.32,1);
        filter: brightness(0.85);
    }
    .gallery-card:hover .card-image {
        transform: scale(1.08);
        filter: brightness(1);
    }
    .card-content-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 50px 30px 25px 30px;
        background: linear-gradient(transparent 0%, rgba(0,0,0,0.95) 100%);
        color: #fff;
        border-radius: 0 0 2px 2px;
        transform: translateY(20px);
        opacity: 0;
        transition: all 0.8s cubic-bezier(.23,1,.32,1);
    }
    .gallery-card:hover .card-content-overlay {
        transform: translateY(0);
        opacity: 1;
    }
    .card-category {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.2em;
        color: #cccccc;
        margin-bottom: 12px;
        font-weight: 400;
    }
    .card-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 300;
        color: #fff;
        margin-bottom: 15px;
        line-height: 1.2;
        word-wrap: break-word;
    }
    .card-description {
        font-size: 1rem;
        color: #cccccc;
        line-height: 1.6;
        max-width: 100%;
        font-weight: 300;
        margin-bottom: 20px;
    }
    .view-gallery-btn {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        color: #fff;
        text-decoration: none;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.15em;
        font-weight: 400;
        padding: 12px 0;
        border-bottom: 1px solid rgba(255,255,255,0.3);
        transition: all 0.4s ease;
    }
    .view-gallery-btn:hover {
        border-bottom: 1px solid #fff;
        letter-spacing: 0.2em;
        padding-right: 20px;
    }

    /* About Section - Mobile Optimized */
    .about-section {
        max-width: 1000px;
        margin: 100px auto 80px;
        padding: 0 20px;
        text-align: center;
    }
    .about-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 300;
        color: #fff;
        margin-bottom: 30px;
        letter-spacing: 0.1em;
        padding-top: 40px;
        word-wrap: break-word;
    }
    .about-description {
        font-size: 1.1rem;
        color: #888;
        line-height: 1.7;
        margin: 0 auto 40px;
        max-width: 100%;
        font-weight: 300;
    }
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 30px;
        margin-top: 60px;
    }
    .stat-item {
        text-align: center;
        padding: 25px 15px;
        border-radius: 2px;
        transition: all 0.3s ease;
    }
    .stat-item:hover {
        background: rgba(255, 255, 255, 0.03);
    }
    .stat-number {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        font-weight: 300;
        color: #fff;
        margin-bottom: 12px;
        line-height: 1;
    }
    .stat-label {
        font-size: 0.85rem;
        color: #888;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        font-weight: 400;
    }

    /* Contact Section - Mobile Optimized */
    .contact-section {
        max-width: 1000px;
        margin: 100px auto 80px;
        padding: 0 20px;
        text-align: center;
    }
    .contact-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 300;
        color: #fff;
        margin-bottom: 30px;
        letter-spacing: 0.1em;
        padding-top: 40px;
        word-wrap: break-word;
    }
    .footer-contact {
        color: #666;
        font-size: 0.9rem;
        margin-bottom: 40px;
        line-height: 1.6;
        font-weight: 400;
    }

    /* Footer - Mobile Optimized */
    .footer {
        border-top: 1px solid rgba(255,255,255,0.08);
        padding: 80px 0 40px;
        margin-top: 120px;
        position: relative;
        background: #0a0a0a;
    }
    .footer::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    }
    .footer-content {
        max-width: 1000px;
        margin: 0 auto;
        text-align: center;
        padding: 0 20px;
    }
    .footer-logo {
        font-family: 'Cinzel', serif;
        font-size: 1.8rem;
        color: #fff;
        margin-bottom: 20px;
        letter-spacing: 0.25em;
        word-wrap: break-word;
    }
    .footer-tagline {
        font-size: 1rem;
        color: #888;
        margin-bottom: 40px;
        max-width: 100%;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.5;
        font-weight: 300;
    }
    .footer-bottom {
        border-top: 1px solid rgba(255,255,255,0.08);
        padding-top: 25px;
        color: #444;
        font-size: 0.8rem;
        letter-spacing: 0.05em;
        line-height: 1.4;
    }

    /* Enhanced Mobile Responsive Design */
    @media (max-width: 1024px) {
        .hero-main-title {
            font-size: 3rem;
            letter-spacing: 0.25em;
        }
        .hero-subtitle {
            font-size: 1.1rem;
            letter-spacing: 0.25em;
        }
        .card-title {
            font-size: 2rem;
        }
        .card-image-wrapper {
            height: 60vh;
            min-height: 450px;
        }
    }

    @media (max-width: 768px) {
        .main-nav {
            padding: 15px 0;
        }
        .nav-content {
            padding: 0 15px;
        }
        .nav-logo {
            font-size: 1.2rem;
            letter-spacing: 0.2em;
        }
        .nav-links {
            gap: 10px;
        }
        .nav-button {
            padding: 8px 15px;
            font-size: 0.75rem;
            letter-spacing: 0.08em;
        }

        .hero-section {
            padding: 130px 0 60px 0;
            margin-top: -70px;
            min-height: 90vh;
        }
        .hero-main-title {
            font-size: 2.2rem;
            letter-spacing: 0.2em;
            margin-bottom: 1rem;
            margin-top: -5px;
        }
        .hero-subtitle {
            font-size: 0.95rem;
            letter-spacing: 0.2em;
            margin-bottom: 2rem;
        }
        .camera-icon {
            font-size: 3rem;
            margin-bottom: 20px;
        }
        .photography-badge {
            padding: 12px 20px;
            gap: 10px;
        }
        .badge-text {
            font-size: 0.8rem;
        }

        .gallery-section {
            padding: 40px 10px 0 10px;
        }
        .gallery-card {
            margin: 60px 0;
        }
        .card-image-wrapper {
            height: 50vh;
            min-height: 350px;
        }
        .card-content-overlay {
            padding: 40px 20px 20px 20px;
        }
        .card-title {
            font-size: 1.8rem;
        }
        .card-description {
            font-size: 0.95rem;
            line-height: 1.5;
        }

        .about-section, .contact-section {
            margin: 80px auto 60px;
            padding: 0 15px;
        }
        .about-title, .contact-title {
            font-size: 1.8rem;
            padding-top: 30px;
        }
        .about-description {
            font-size: 1rem;
        }

        .stats-grid {
            grid-template-columns: 1fr;
            gap: 20px;
            margin-top: 40px;
        }
        .stat-item {
            padding: 20px 15px;
        }
        .stat-number {
            font-size: 2rem;
        }

        .footer {
            padding: 60px 0 30px;
            margin-top: 80px;
        }
        .footer-logo {
            font-size: 1.5rem;
        }
        .section-anchor {
            top: -60px;
        }
    }

    @media (max-width: 480px) {
        .nav-content {
            padding: 0 10px;
        }
        .nav-logo {
            font-size: 1rem;
            letter-spacing: 0.15em;
        }
        .nav-button {
            padding: 6px 12px;
            font-size: 0.7rem;
        }

        .hero-section {
            padding: 120px 0 50px 0;
            margin-top: -60px;
            min-height: 85vh;
        }
        .hero-main-title {
            font-size: 1.8rem;
            letter-spacing: 0.15em;
        }
        .hero-subtitle {
            font-size: 0.85rem;
            letter-spacing: 0.15em;
        }
        .camera-icon {
            font-size: 2.5rem;
        }
        .photography-badge {
            padding: 10px 15px;
        }
        .badge-text {
            font-size: 0.75rem;
        }
        .scroll-indicator {
            font-size: 0.7rem;
            bottom: 30px;
        }

        .gallery-card {
            margin: 40px 0;
        }
        .card-image-wrapper {
            height: 40vh;
            min-height: 280px;
        }
        .card-content-overlay {
            padding: 30px 15px 15px 15px;
        }
        .card-title {
            font-size: 1.5rem;
        }
        .card-description {
            font-size: 0.9rem;
        }
        .view-gallery-btn {
            font-size: 0.8rem;
        }

        .about-title, .contact-title {
            font-size: 1.5rem;
        }
        .about-description {
            font-size: 0.95rem;
        }

        .footer-logo {
            font-size: 1.3rem;
        }
        .footer-tagline {
            font-size: 0.9rem;
        }
        .section-anchor {
            top: -50px;
        }

        /* Hide lens flare on very small devices for performance */
        .lens-flare, .lens-flare-2 {
            display: none;
        }
    }

    @media (max-width: 360px) {
        .hero-main-title {
            font-size: 1.5rem;
        }
        .nav-links {
            gap: 5px;
        }
        .nav-button {
            padding: 5px 10px;
            font-size: 0.65rem;
        }
        .card-title {
            font-size: 1.3rem;
        }
    }

    /* Touch device optimizations */
    @media (hover: none) {
        .gallery-card:hover .card-image {
            transform: none;
        }
        .gallery-card:hover .card-content-overlay {
            transform: translateY(0);
            opacity: 1;
        }
        .card-content-overlay {
            transform: translateY(0);
            opacity: 1;
            background: linear-gradient(transparent 0%, rgba(0,0,0,0.85) 100%);
        }
    }

    /* Prevent horizontal scrolling */
    html, body {
        max-width: 100%;
        overflow-x: hidden;
    }
</style>
""", unsafe_allow_html=True)

# Navigation Bar
st.markdown("""
<!-- Navigation -->
<div class="main-nav">
    <div class="nav-content">
        <a href="#" class="nav-logo">SoulShutter</a>
        <div class="nav-links">
            <a href="#portfolio" class="nav-button">Portfolio</a>
            <a href="#about" class="nav-button">About</a>
            <a href="#contact" class="nav-button">Contact</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <div class="lens-flare"></div>
    <div class="lens-flare-2"></div>
    <div class="hero-content">
        <div class="camera-icon">📸</div>
        <div class="hero-main-title">SOULSHUTTER</div>
        <div class="hero-subtitle">Photography Studio</div>
        <div class="photography-badge">
            <span class="badge-icon">❤️🎗️</span>
            <span class="badge-text">Professional Photography</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Portfolio Section
st.markdown('<div class="section-anchor" id="portfolio"></div>', unsafe_allow_html=True)
st.markdown('<div class="gallery-section">', unsafe_allow_html=True)

galleries = [
    {
        "category": "Landscape Photography",
        "title": "Sky & Atmosphere",
        "description": "Dramatic cloud formations and breathtaking celestial moments captured with technical precision and artistic vision.",
        "image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?ixlib=rb-4.0.3&w=1200",
        "link": "https://orchid85.pixieset.com/sky/"
    },
    {
        "category": "Macro Photography",
        "title": "Botanical Elegance",
        "description": "Intimate portraits of nature's delicate beauty, revealing intricate details often overlooked by the naked eye.",
        "image": "https://images.unsplash.com/photo-1490750967868-88aa4486c946?ixlib=rb-4.0.3&w=1200",
        "link": "https://orchid85.pixieset.com/flower/"
    },
    {
        "category": "Portrait Series",
        "title": "Human Moments",
        "description": "Authentic emotional portraits and candid moments that tell stories of human experience and connection.",
        "image": "https://images.unsplash.com/photo-1489710437720-ebb67ec84dd2?ixlib=rb-4.0.3&w=1200",
        "link": "https://orchid85.pixieset.com/moments/"
    }
]

for gallery in galleries:
    st.markdown(f"""
    <div class="gallery-card">
        <div class="card-image-wrapper">
            <img src="{gallery['image']}" class="card-image" alt="{gallery['title']}" loading="lazy">
            <div class="card-content-overlay">
                <div class="card-category">{gallery['category']}</div>
                <div class="card-title">{gallery['title']}</div>
                <div class="card-description">{gallery['description']}</div>
                <a href="{gallery['link']}" target="_blank" class="view-gallery-btn">
                    View Gallery <span>→</span>
                </a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# About Section
st.markdown('<div class="section-anchor" id="about"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="about-section">
    <div class="about-title">About the Artist</div>
    <div class="about-description">
        With an engineering background and a passion for visual storytelling, each project is approached with precision and creative intuition. The mission: to capture the essence of a moment, transforming ordinary scenes into extraordinary visual narratives.
    </div>
    <div class="stats-grid">
        <div class="stat-item">
            <div class="stat-number">100+</div>
            <div class="stat-label">Projects Completed</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">4</div>
            <div class="stat-label">Years Experience</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">100%</div>
            <div class="stat-label">Client Satisfaction</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown('<div class="section-anchor" id="contact"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="contact-section">
    <div class="contact-title">Get In Touch</div>
    <div class="about-description">
        Ready to capture your special moments? Let's discuss your photography needs and create something memorable together. Where engineering precision meets artistic vision.
    </div>
    <div class="footer-contact">
        📧 hello@soulshutter.com<br>
        📍 Available for projects worldwide
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <div class="footer-content">
        <div class="footer-logo">SOULSHUTTER</div>
        <div class="footer-tagline">
            Capturing the world through a lens of technical excellence and artistic vision. Where every click tells a story.
        </div>
        <div class="footer-contact">
            📧 hello@soulshutter.com<br>
            📍 Available for projects worldwide
        </div>
        <div class="footer-bottom">
            © 2024 SoulShutter Photography Studio. All rights reserved. | Crafted with precision and passion
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# JavaScript for smooth navigation scroll with mobile support
st.markdown("""
<script>
document.querySelectorAll('.nav-button').forEach(button => {
    button.addEventListener('click', function(e) {
        e.preventDefault();
        var targetId = button.getAttribute('href').substring(1);
        var targetElement = document.getElementById(targetId);
        if (targetElement) {
            var offsetTop = targetElement.offsetTop - 80;
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// Mobile touch improvements
document.addEventListener('touchstart', function() {}, {passive: true});

// Prevent zoom on double tap
let lastTouchEnd = 0;
document.addEventListener('touchend', function (event) {
    const now = (new Date()).getTime();
    if (now - lastTouchEnd <= 300) {
        event.preventDefault();
    }
    lastTouchEnd = now;
}, false);
</script>
""", unsafe_allow_html=True)