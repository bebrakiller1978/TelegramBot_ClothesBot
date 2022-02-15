import json


ListOfSizes = [
    {'male':{'evro':''   ,'USA':''  ,'rus':''  }, 'female':{'evro':'XXS','USA':'24','rus':'38'} },  #  78-84
    {'male':{'evro':''   ,'USA':''  ,'rus':''  }, 'female':{'evro':'XS' ,'USA':'25','rus':'40'} },  #  85-87
    {'male':{'evro':''   ,'USA':''  ,'rus':''  }, 'female':{'evro':'S'  ,'USA':'26','rus':'42'} },  #  88-90
    {'male':{'evro':'XS' ,'USA':'28','rus':'44'}, 'female':{'evro':'S'  ,'USA':'27','rus':'42'} },  #  91-93
    {'male':{'evro':'XS' ,'USA':'29','rus':'44'}, 'female':{'evro':'M'  ,'USA':'28','rus':'44'} },  #  94-96
    {'male':{'evro':'S'  ,'USA':'31','rus':'46'}, 'female':{'evro':'M'  ,'USA':'29','rus':'44'} },  #  97-99
    {'male':{'evro':'M'  ,'USA':'33','rus':'48'}, 'female':{'evro':'L'  ,'USA':'30','rus':'46'} },  # 100-102	
    {'male':{'evro':'L'  ,'USA':'34','rus':'50'}, 'female':{'evro':'L'  ,'USA':'31','rus':'48'} },  # 103-105
    {'male':{'evro':'L'  ,'USA':'35','rus':'50'}, 'female':{'evro':'XL' ,'USA':'32','rus':'50'} },  # 106-108
    {'male':{'evro':'XL ','USA':'37','rus':'52'}, 'female':{'evro':'XL' ,'USA':'33','rus':'50'} },  # 109-111	
    {'male':{'evro':'XXL','USA':'38','rus':'54'}, 'female':{'evro':'XXL','USA':'34','rus':'54'} },  # 112-114
    {'male':{'evro':'3XL','USA':'40','rus':'56'}, 'female':{'evro':'XXL','USA':'35','rus':'54'} },  # 115	
    {'male':{'evro':'4XL','USA':'42','rus':'58'}, 'female':{'evro':'3XL','USA':'36','rus':'56'} },  # 116-118	  
    {'male':{'evro':'5XL','USA':'44','rus':'60'}, 'female':{'evro':'3XL','USA':'37','rus':'56'} },  # 118-120
    {'male':{'evro':''   ,'USA':''  ,'rus':''  }, 'female':{'evro':'4XL','USA':'38','rus':'58'} },  # 120-122
    {'male':{'evro':''   ,'USA':''  ,'rus':''  }, 'female':{'evro':'4XL','USA':'39','rus':'58'} },  # 123-126
    {'male':{'evro':''   ,'USA':''  ,'rus':''  }, 'female':{'evro':'5XL','USA':'40','rus':'60'} },  # 127
    {'male':{'evro':''   ,'USA':''  ,'rus':''  }, 'female':{'evro':''   ,'USA':''  ,'rus':''  } },
    {'male':{'evro':''   ,'USA':''  ,'rus':''  }, 'female':{'evro':''   ,'USA':''  ,'rus':''  } },
    {'male':{'evro':''   ,'USA':''  ,'rus':''  }, 'female':{'evro':''   ,'USA':''  ,'rus':''  } },
    {'male':{'evro':''   ,'USA':''  ,'rus':''  }, 'female':{'evro':''   ,'USA':''  ,'rus':''  } }
]




jsonString = json.dumps(ListOfSizes)
jsonFile = open("dataSize.json", "w")
jsonFile.write(jsonString)
jsonFile.close() 

