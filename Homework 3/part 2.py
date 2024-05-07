import turtle

def koch_snowflake(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(order-1, size/3)
            turtle.left(angle)

def main():
    recursion_level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))

    # Налаштування вікна Turtle
    window = turtle.Screen()
    window.bgcolor("white")
    turtle.speed(0)  
    turtle.penup()
    turtle.goto(-150, 90)
    turtle.pendown()
    
    for _ in range(3):
        koch_snowflake(recursion_level, 300)
        turtle.right(120)
    
    turtle.hideturtle()
    window.mainloop()

if __name__ == "__main__":
    main()
