function calculate() {
		var currentPrice = document.getElementById('currentPrice').innerHTML;	
		var quantity = document.getElementById('numOfShares').value;
		var result = document.getElementById('totalCost');	
		var myResult = currentPrice * quantity;
		result.textContent= '$' + parseFloat(Math.round(myResult*100) /100).toFixed(2);
      
		
	}
function getTotalCost() {
	var button = document.getElementById('buyButton');	
	var result = document.getElementById('totalCost');	
    button.value = result.textContent.replace('$', '').trim();
}