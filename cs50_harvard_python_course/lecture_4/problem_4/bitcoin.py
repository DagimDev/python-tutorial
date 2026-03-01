import sys
import requests

def main():
    # Check command-line argument
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    
    # Get number of bitcoins from command line
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    
    try:
        # Replace 'YOUR_API_KEY' with your actual CoinCap API key
        api_key = "YOUR_API_KEY"  # ← YOU MUST CHANGE THIS!
        
        # Query the CoinCap API for Bitcoin price
        url = f"https://api.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Parse JSON response
        data = response.json()
        
        # Extract price (priceUsd is a string in the response)
        price_usd = float(data["data"]["priceUsd"])
        
        # Calculate total cost
        total_cost = n * price_usd
        
        # Format output with thousands separator and 4 decimal places
        print(f"${total_cost:,.4f}")
        
    except requests.RequestException:
        sys.exit("Error: Unable to fetch Bitcoin price")
    except (KeyError, ValueError):
        sys.exit("Error: Invalid response from API")


if __name__ == "__main__":
    main()