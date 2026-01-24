// Global fixes for all pages
document.addEventListener('DOMContentLoaded', function() {
    // Fix all partner image paths
    document.querySelectorAll('img[src*="our partners"]').forEach(img => {
        img.src = img.src.replace('our partners', 'partners');
    });
    
    // Add error handling to all images
    document.querySelectorAll('img').forEach(img => {
        img.addEventListener('error', function() {
            if (this.src.includes('partners')) {
                this.src = '../../assets/images/partners/ejendals.jpg';
            } else if (this.src.includes('products')) {
                this.src = '../../assets/images/products/aircraft-belt-loader.png';
            }
        });
    });
    
    // Ensure mobile menu works
    const mobileMenuButton = document.getElementById('mobileMenuButton');
    const mobileMenu = document.getElementById('mobileMenu');
    
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
            const icon = this.querySelector('i');
            if (mobileMenu.classList.contains('hidden')) {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            } else {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            }
        });
    }
});