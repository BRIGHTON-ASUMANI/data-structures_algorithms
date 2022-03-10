

def test(products, productPrices, productSold, soldPrice):
    store = {}
    count = 0

    products = ["eggs", "milk", "cheese"]
    productPrices = [2.89, 3.29, 5.79]
    productSold = ["eggs", "eggs", "cheese", "milk"]
    soldPrice = [2.89, 2.99, 5.97, 3.29]
    for i in range(len(products)):
        store[products[i]] = productPrices[i]

    for j in range(len(productSold)):
        if(store[productSold[j]] != soldPrice[j]):
            count += 1
    return count


print(test(["eggs", "milk", "cheese"], [2.89, 3.29, 5.79], [
      "eggs", "eggs", "cheese", "milk"], [2.89, 2.99, 5.97, 3.29]))
