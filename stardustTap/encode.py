for i in range(1,33):
	with open("new_asset_{:0>2}.mp3".format(i),'rb') as f:
		asset["{}.mp3".format(i-1)] = "data:audio/mp3;base64," + base64.b64encode(f.read()).decode()
with open("main.json","w") as f:
	json.dump(asset,f,indent=0)		
