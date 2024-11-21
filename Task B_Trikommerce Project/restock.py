def restock_inventory(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.


The function will also update the inventory_records (For restocking) for a  given current day. It will also return "available_items".
    '''
    restocked_units = 0                                 # defines and will be used when current_days % 7 != 0
    if current_day == 0:                                
        inventory_records.append([0, 0, 2000, 2000])    # on day 0 stocks up to 2000 originally
    if current_day % 7 == 0 :
        if current_day != 0 :                           # every 7th day excluding day 0, calculates number of items restocked and restocks available items to 2000
            restocked_units = 2000 - available_items
            available_items = 2000
            inventory_records.append([current_day, 0, restocked_units, available_items])        # updates inventory records with the amount restocked and the new available items
    return available_items
