document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('comparison-form');
    const input = document.getElementById('budget-input');
    const button = document.getElementById('compare-button');

    if (form && input && button) {
        form.addEventListener('submit', () => {
            const budgetValue = input.value;
            if (budgetValue && !isNaN(parseFloat(budgetValue)) && parseFloat(budgetValue) > 0) {
                 button.textContent = 'KARŞILAŞTIRILIYOR...';
                 button.disabled = true;

                 button.classList.add('loading'); 
            }
        });
    }
});