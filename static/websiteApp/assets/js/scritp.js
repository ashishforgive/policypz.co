const cardContainer = document.querySelector('.card-container');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
let currentIndex = 0;
let cardsPerPage = calculateCardsPerPage();

function showCards(startIndex) {
    for (let i = 0; i < cardContainer.children.length; i++) {
        const card = cardContainer.children[i];
        if (i >= startIndex && i < startIndex + cardsPerPage) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    }
}

function updateButtonState() {
    if (currentIndex === 0) {
        prevBtn.disabled = true;
        nextBtn.disabled = false;
        prevBtn.style.display = 'none';
    } else if (currentIndex >= cardContainer.children.length - cardsPerPage) {
        prevBtn.disabled = false;
        nextBtn.disabled = true;
        nextBtn.style.display = 'none';
    } else {
        prevBtn.disabled = false;
        nextBtn.disabled = false;
        prevBtn.style.display = 'block';
        nextBtn.style.display = 'block';
    }
}

function nextCards() {
    currentIndex = (currentIndex + 1) % cardContainer.children.length;
    showCards(currentIndex);
    updateButtonState();
}

function prevCards() {
    currentIndex = (currentIndex - 1 + cardContainer.children.length) % cardContainer.children.length;
    showCards(currentIndex);
    updateButtonState();
}

function calculateCardsPerPage() {
    const screenWidth = window.innerWidth;
    if (screenWidth < 576) {
        return 1; // Mobile: Show 1 card per page
    } else if (screenWidth < 992) {
        return 3; // Tablet: Show 3 cards per page
    } else {
        return 5; // Desktop: Show 5 cards per page
    }
}

// Add event listeners to adjust the number of cards when the window is resized
window.addEventListener('resize', () => {
    const newCardsPerPage = calculateCardsPerPage();
    if (newCardsPerPage !== cardsPerPage) {
        cardsPerPage = newCardsPerPage;
        currentIndex = 0; // Reset to the first card when the number of cards per page changes
        showCards(currentIndex);
        updateButtonState();
    }
});

nextBtn.addEventListener('click', nextCards);
prevBtn.addEventListener('click', prevCards);

showCards(currentIndex);
updateButtonState();