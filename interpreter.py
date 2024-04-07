def main():
 expression = input("Enter an arithmetic expression (format: x y z): ")  
 x, operator, z = expression.split() 
 x = int(x) 
 z = int(z)  
 if operator == '+':
        result = x + z 
 elif operator == '-':
        result = x - z
 elif operator == '*':
        result = x * z
 elif operator == '/':
        result = x / z
 print(f"Result: {result:.1f}")

if __name__ == "__main__":
    main()
