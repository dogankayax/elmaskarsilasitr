document.addEventListener('DOMContentLoaded', function() {
    console.log('MLBB Elmas Fiyat Karşılaştırma sitesi yüklendi!');
    
    const loginBtn = document.querySelector('.login-btn');
    if (loginBtn) {
        loginBtn.addEventListener('click', function(e) {
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
            
            console.log('Sisteme giriş butonuna tıklandı');
        });
    }
    
    const sellerCards = document.querySelectorAll('.seller-card');
    sellerCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    setTimeout(() => {
        console.log('MLBB Elmas Fiyat Karşılaştırma sistemine hoş geldiniz!');
    }, 1000);
    
    function initMobileMenu() {
        console.log('Mobil menü başlatıldı');
    }
    
    window.addEventListener('resize', function() {
        console.log('Pencere boyutu değişti: ' + window.innerWidth + 'x' + window.innerHeight);
    });
    
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const parallaxElements = document.querySelectorAll('.section');
        
        parallaxElements.forEach(element => {
            const speed = 0.5;
            const yPos = -(scrolled * speed);
            element.style.backgroundPosition = `center ${yPos}px`;
        });
    });
});