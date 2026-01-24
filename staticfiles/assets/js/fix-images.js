// Quick fix for all partner images
document.addEventListener('DOMContentLoaded', function() {
    // Fix partner images
    const partnerImages = document.querySelectorAll('img[src*="our partners"]');
    partnerImages.forEach(img => {
        const newSrc = img.src.replace('our partners', 'partners');
        img.src = newSrc;
        img.onerror = function() {
            // Fallback to available images
            const fallbacks = [
                'assets/images/partners/ejendals.jpg',
                'assets/images/partners/Honeywell.jpg',
                'assets/images/partners/Polaris.jpg',
                'assets/images/partners/aero-homepage.jpg',
                'assets/images/partners/homepage-eagle.jpg',
                'assets/images/partners/homepage-pci.jpg'
            ];
            this.src = fallbacks[Math.floor(Math.random() * fallbacks.length)];
        };
    });
    
    // Fix missing product images
    const productImages = document.querySelectorAll('img[src*="products"]');
    productImages.forEach(img => {
        img.onerror = function() {
            // Use a placeholder or existing image
            this.src = 'assets/images/products/aircraft-belt-loader.png';
        };
    });
});