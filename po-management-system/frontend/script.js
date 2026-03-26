function addRow(){

let table = document.getElementById("productTable");

let row = table.insertRow();

row.innerHTML = `
<td>
<select>
<option>Product 1</option>
<option>Product 2</option>
</select>
</td>

<td><input type="number"></td>
<td><input type="number"></td>
`;

}