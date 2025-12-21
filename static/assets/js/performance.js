// Performance optimizations
(function() {
    'use strict';
    
    // Lazy load images
    function lazyLoadImages() {
        const images = document.querySelectorAll('img[data-src]');
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        images.forEach(img => imageObserver.observe(img));
    }
    
    // Preload critical resources
    function preloadCritical() {
        const criticalImages = [
            'assets/images/hero/banner-large-opt.jpg',
            'assets/images/partners/ejendals.jpg',
            'assets/images/partners/Honeywell.jpg'
        ];
        
        criticalImages.forEach(src => {
            const link = document.createElement('link');
            link.rel = 'preload';
            link.as = 'image';
            link.href = src;
            document.head.appendChild(link);
        });
    }
    
    // Fix broken images
    function fixBrokenImages() {
        document.querySelectorAll('img').forEach(img => {
            img.addEventListener('error', function() {
                if (this.src.includes('our partners')) {
                    this.src = 'assets/images/partners/ejendals.jpg';
                } else if (this.src.includes('products')) {
                    this.src = 'assets/images/products/aircraft-belt-loader.png';
                }
            });
        });
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            lazyLoadImages();
            preloadCritical();
            fixBrokenImages();
        });
    } else {
        lazyLoadImages();
        preloadCritical();
        fixBrokenImages();
    }
})();