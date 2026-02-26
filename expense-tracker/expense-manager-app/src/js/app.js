const expenses = [];
const expenseList = document.getElementById('expense-list');
const totalAmount = document.getElementById('total-expenses');
const expenseForm = document.getElementById('expense-form');
const expenseInput = document.getElementById('expense-name');
const amountInput = document.getElementById('expense-amount');

function addExpense(event) {
    event.preventDefault();
    
    const expense = expenseInput.value;
    const amount = parseFloat(amountInput.value);
    
    if (expense && !isNaN(amount) && amount > 0) {
        expenses.push({ expense, amount });
        updateExpenseList();
        updateTotalAmount();
        expenseForm.reset();
    } else {
        alert('Please enter a valid expense and amount.');
    }
}

function removeExpense(index) {
    expenses.splice(index, 1);
    updateExpenseList();
    updateTotalAmount();
}

function updateExpenseList() {
    expenseList.innerHTML = '';
    expenses.forEach((item, index) => {
        const li = document.createElement('li');
        li.className = 'list-group-item d-flex justify-content-between align-items-center';
        li.textContent = `${item.expense}: $${item.amount.toFixed(2)}`;
        
        const removeButton = document.createElement('button');
        removeButton.className = 'btn btn-danger btn-sm';
        removeButton.textContent = 'Remove';
        removeButton.onclick = () => removeExpense(index);
        
        li.appendChild(removeButton);
        expenseList.appendChild(li);
    });
}

function updateTotalAmount() {
    const total = expenses.reduce((sum, item) => sum + item.amount, 0);
    totalAmount.textContent = `$${total.toFixed(2)}`;
}

expenseForm.addEventListener('submit', addExpense);