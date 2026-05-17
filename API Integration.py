import requests

def get_crypto_price(crypto_name):  #Functio to fetch cryptocurrency price 
    
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_name}&vs_currencies=usd"   #API URL

    try:
        response = requests.get(url)

        if response.status_code == 200:      #Check if request was successful 

            data = response.json()   #Covert JSON response into Python dictionary

            if crypto_name in data:               #Check if cryptocurrency exits 
                price = data[crypto_name]["usd"]

                print("\n Cryptocurrency Price")
                print("---------------------------")
                print(f"Crypto Name : {crypto_name.upper()}")
                print(f"Price (USD) : ${price}")

            else:
                print("Invalid cryptocurrency name.")

        else:
            print("Failed to fetch data from API.")

    
    except requests.exceptions.RequestException as e:    #Handle connection errors
        print("Error:", e)



print("===== Cryptocurrency Price Tracker =====")     #Main Program 

crypto = input("Enter cryptocurrency name (bitcoin, ethereum, dogecoin): ").lower()

get_crypto_price(crypto)