function loadExpenses() {
    fetch('/expenses')
        .then(response => response.json())
        .then(data => {
            const expensesDiv = document.getElementById('expenses');
            expensesDiv.innerHTML = '';

            if (data.length === 0) {
                expensesDiv.innerHTML = '<p>No expenses found.</p>';
            } else {
                data.forEach(expense => {
                    const expenseDiv = document.createElement('div');
                    expenseDiv.className = 'expense';
                    expenseDiv.innerHTML = `
                        <p>Date: ${expense[0]}</p>
                        <p>Category: ${expense[1]}</p>
                        <p>Description: ${expense[2]}</p>
                        <p>Amount: ${expense[3]}</p>
                    `;
                    expensesDiv.appendChild(expenseDiv);
                });
            }
        });
}
