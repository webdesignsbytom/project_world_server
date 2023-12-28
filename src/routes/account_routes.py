from flask import Blueprint
from controllers.account_controller import get_all_accounts, create_new_account, delete_account
from utilities.response_util import sendDataResponse, sendMessageResponse

account_blueprint = Blueprint('account_blueprint', __name__)

# Get all accounts
@account_blueprint.route('/get-all-accounts', methods=['GET'])
def get_all_accounts_route():
    try:
        foundAccounts = get_all_accounts()
        if not foundAccounts:
            return sendMessageResponse('Accounts not found', 404)  
        
        return sendDataResponse({'Found Accounts: ': foundAccounts}, 200)  
    except Exception as e:
        return sendMessageResponse(str(e), 500) 


# Create a new account  
@account_blueprint.route('/create-new-account', methods=['POST'])
def create_new_account_route():
    try:
        newCreatedAccount = create_new_account()
        print("Created new account: " + newCreatedAccount)
        
        if not newCreatedAccount:
            return sendMessageResponse('Accounts not created', 404)  
        
        return sendDataResponse({"message": "Account created successfully"}, 201)
    except Exception as e:
        return sendDataResponse("str(e)", 500)


# Delete account  
@account_blueprint.route('/delete-account/<account_id>', methods=['DELETE'])
def delete_account_route(account_id):
    try:
        deletedAccount = delete_account(account_id)
        
        if not deletedAccount:
            return sendMessageResponse('Account not found or not deleted', 404)
        
        return sendDataResponse({"message": "Account deleted successfully"}, 200)
    except Exception as e:
        return sendMessageResponse(str(e), 500)

    


   
   
