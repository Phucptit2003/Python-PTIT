<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Shopping Cart</title>
</head>
<body>
    <h1>Shopping Cart</h1>
    <table border="1">
        <tr>
            <th>Product ID</th>
            <th>Product Name</th>
            <th>Quantity</th>
            <th>Price</th>
            <th>Total</th>
            <th>Action</th>
        </tr>
        <c:forEach items="${cart}" var="item">
            <tr>
                <td>${item.productID}</td>
                <td>${item.productName}</td>
                <td>
                    <form action="cart" method="post">
                        <input type="hidden" name="action" value="update">
                        <input type="hidden" name="productID" value="${item.productID}">
                        <input type="number" name="quantity" value="${item.quantity}">
                        <input type="submit" value="Update">
                    </form>
                </td>
                <td>${item.price}</td>
                <td>${item.quantity * item.price}</td>
                <td>
                    <form action="cart" method="post">
                        <input type="hidden" name="action" value="remove">
                        <input type="hidden" name="productID" value="${item.productID}">
                        <input type="submit" value="Remove">
                    </form>
                </td>
            </tr>
        </c:forEach>
    </table>
    <p>Total: $<c:out value="${totalPrice}" /></p>
    <a href="checkout.jsp">Checkout</a>
</body>
</html>
