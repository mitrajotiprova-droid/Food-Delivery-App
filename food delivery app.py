import gradio as gr

menu = {
    "Pizza": 250,
    "Burger": 120,
    "Pasta": 180,
    "Sandwich": 100,
    "French Fries": 90
}

def place_order(item, quantity):
    quantity = int(quantity)
    total = menu[item] * quantity

    return f"""
    Order Confirmed!

    Item: {item}
    Quantity: {quantity}
    Price per Item: ₹{menu[item]}
    Total Amount: ₹{total}

    Thank you for ordering!
    """

app = gr.Interface(
    fn=place_order,
    inputs=[
        gr.Dropdown(list(menu.keys()), label="Select Food Item"),
        gr.Number(label="Quantity", value=1)
    ],
    outputs=gr.Textbox(label="Order Details"),
    title="Food Delivery App",
    description="Order your favorite food online"
)

app.launch()
