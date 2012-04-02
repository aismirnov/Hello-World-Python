import VK
api_secret = 'qwertyuifghjk'
api_id = '123456'
VK = VK.VKReq(api_id, api_secret)
friends_req = VK.get({'uid': 123456, 'count': 500, 'fields': 'uid,first_name,last_name,photo,photo_big', 'method': 'friends.get'})
