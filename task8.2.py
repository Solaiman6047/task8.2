def bread_price(n,ob):
    regular_price=n*3.49
    discount=((ob*6)*3.49)/100
    total=regular_price-discount
    return regular_price, discount, total

n=int(input("Enter the number of bread: "))
ob=int(input("Enter the number of old bread: "))
price,after_discount,total=bread_price(n,ob)
print(f"regular price={price}, the discount={after_discount}, total={total}")