from models import * 

import os


def del_old_db():
    db_path = os.path.join(os.getcwd(), "betsy.db")
    if os.path.exists(db_path):
        os.remove(db_path)

def populate_db():

    db.connect()
    db.create_tables([User, Product, Address, BillInfo, Tag, TagHanger, TransactionDetail])

    bob_address = Address.create(streetname="Lameroen", 
                                 number=41,
                                 zipcode="1141ZW",
                                 city="Monnickendam",
                                 country="NL"
                                 )
    bob_billing_info = BillInfo.create(billing_address=bob_address,
                                       iban="FO86 8807 3164 5544 73"
                                       )
    bob_user = User.create(fullname="Bob de Vries", 
                           address=bob_address,
                           billing_info=bob_billing_info
                           )


    hans_address = Address.create(streetname="Mitchell Park", 
                                 number=6852 ,
                                 zipcode="5848PP",
                                 city="Duskolpinkerstal",
                                 country="NL"
                                 )
    hans_billing_info = BillInfo.create(billing_address=hans_address,
                                       iban="MK47 974C GTB3 M81S I12"
                                       )
    hans_user = User.create(fullname="Hans Pinky", 
                           address=hans_address,
                           billing_info=hans_billing_info
                           )



    marieke_address = Address.create(streetname="Donald Place", 
                                 number=213,
                                 number_add="3h",
                                 zipcode="1877AP",
                                 city="Joekelsdam",
                                 country="NL"
                                 )
    marieke_billing_info = BillInfo.create(billing_address=marieke_address,
                                       iban="RS17 3706 0712 0392 7672 35"
                                       )
    marieke_user = User.create(fullname="Marieke Opperhouser", 
                           address=marieke_address,
                           billing_info=marieke_billing_info
                           )


    hong_address = Address.create(streetname="Bowman Avenue", 
                                 number=2 ,
                                 zipcode="1011PP",
                                 city="Amsterdam",
                                 country="NL"
                                 )
    hong_billing_info = BillInfo.create(billing_address=hong_address,
                                       iban="LT91 0386 7630 9463 2295"
                                       )
    hong_user = User.create(fullname="Hong Lee Ai", 
                           address=hong_address,
                           billing_info=hong_billing_info
    )
    
    wooden = Tag.create(name = 'wooden')
    furniture = Tag.create(name = 'furniture')
    cotton = Tag.create(name = 'cotton')
    polyester = Tag.create(name = 'polyester')
    spicy = Tag.create(name = 'ecofriendly')
    sweet = Tag.create(name = 'sweet')
    sour = Tag.create(name = 'sour')
    food = Tag.create(name = 'food')
    toy = Tag.create(name = 'toy')
    doll = Tag.create(name = 'doll')
    fleece = Tag.create(name = 'fleece')
    clothing = Tag.create(name = 'clothing')
    metal = Tag.create(name = 'metal')
    
    bobs_chair = Product.create(
                                 owner=bob_user, 
                                 name="Chair",
                                 description="A low, compact chair that is perfect for small spaces. The comfort is firm and supportive and the back low to rest the arms upon; the back is sprung, well padded and hand buttoned and further softened with a fully sprung seat and luxurious feather-wrapped foam seat interior. Each hand-crafted frame is made from sustainable hardwoods and double or triple dowelled, glued and screwed, with corner blocks for extra rigidity. Our robust construction ensures that our frames will last a lifetime.",
                                 price_per_product=160.00,
                                 quantity=8,
    )
    
    TagHanger.create(tagged = bobs_chair, tag = wooden)
    TagHanger.create(tagged = bobs_chair, tag = furniture)

    bobs_table = Product.create(
                                 owner=bob_user, 
                                 name="Table",
                                 description="Extending handmade table with solid wood top and a choice of leg options. This table has 50cm extensions which simply slide in at the end(s). They are long enough to allow for a place setting without a table leg intruding. The table top is made in one piece and then cut so the wood grain matches once the extensions are in place.",
                                 price_per_product=800.00,
                                 quantity=2,  

    )
    
    TagHanger.create(tagged = bobs_table, tag = wooden)
    TagHanger.create(tagged = bobs_table, tag = furniture)


    bobs_sofa = Product.create(
                                 owner=bob_user, 
                                 name="Sofa",
                                 description="A supremely comfortable shape, with exquisite detailing in the hand buttoned seat and back that gives a formal old-school glamour to interior schemes. The Fairbanks has a deep, coil sprung seat, softened with foam and quilting to give a buoyant, supportive comfort. Each hand-crafted frame is made from sustainable hardwoods and double or triple dowelled, glued and screwed, with corner blocks for extra rigidity. Our robust construction ensures that our frames will last a lifetime. This Grand Fairbanks measures 217cm wide x 89cm high x 106cm deep and is covered in Bernini Kingfisher; a cosy, velvet chenille with a subtle lustre and incredibly soft handle. Feet are hand-polished with our Blackened Oak finish. Fabric composition; 62% Polyester, 38% Cotton.",
                                 price_per_product=3000.00,
                                 quantity=4,
                                 )
    
    TagHanger.create(tagged = bobs_sofa, tag = furniture)
    TagHanger.create(tagged = bobs_sofa, tag = cotton)
    TagHanger.create(tagged = bobs_sofa, tag = polyester)


    hans_doll = Product.create(
                                 owner=hans_user, 
                                 name="Doll",
                                 description="The Hansie The Doll is made using premium 100% cotton yarn, and is stuffed with hypoallergenic polyester filling. Ola is hand-knit and hand-loomed, and is made to withstand a lifetime of love and play!",
                                 price_per_product=50.95,
                                 quantity=2,
                                 )
    
    TagHanger.create(tagged = hans_doll, tag = toy)
    TagHanger.create(tagged = hans_doll, tag = cotton)
    TagHanger.create(tagged = hans_doll, tag = doll)

    hans_doll_house = Product.create(
                                 owner=hans_user, 
                                 name="Dollhouse",
                                 description="Hansies Villa Dolls House. Hansies Villa is a grand townhouse. A perfect mid-size dolls house full of stylish furniture, it is based on a classic terraced house - but instead of brick, Hansies Villa is made from a beautiful birch plywood giving the dolls house a softer look and natural tactile feel.",
                                 price_per_product=120.00,
                                 quantity=1,
                                 )

    TagHanger.create(tagged = hans_doll_house, tag = furniture)
    TagHanger.create(tagged = hans_doll_house, tag = doll)
    TagHanger.create(tagged = hans_doll_house, tag = wooden)

    hans_clock = Product.create(
                                 owner=hans_user, 
                                 name="Clock",
                                 description="This charming, playful and handmade clock will make a wonderful addition to any nursery, bedroom, playroom, or kitchen wall. Every morning will be a cheery one with Penny Panda and she’ll provide a fun way to teach your children to tell the time.",
                                 price_per_product=25.00,
                                 quantity=4,
                                )
    
    TagHanger.create(tagged = hans_clock, tag = furniture)
    TagHanger.create(tagged = hans_clock, tag = wooden)

    marieke_pants = Product.create(
                                 owner=marieke_user, 
                                 name="Pants",
                                 description="Pants in a nice dark dove blue colour, slightly high-waisted, with a bit of stretch. The trousers are a straight model with quite a bit of width. The trousers have belt straps and a nice seam in the middle that gives a classic look. The trousers are made of soft material that is really comfortable and sits very well on the body.",
                                 price_per_product=59.99,
                                 quantity=100, 
                                )
    
    TagHanger.create(tagged = marieke_pants, tag = clothing)
    TagHanger.create(tagged = marieke_pants, tag = cotton)

    marieke_sweater = Product.create(
                                 owner=marieke_user, 
                                 name="Sweater",
                                 description="Oversized sweatshirt with zipper in ta very soft material. The sweatshirt has fleece inside and is so soft to wear. VDB is embroidered on.",
                                 price_per_product=30.99,
                                 quantity=50, 
                                 )
    
    TagHanger.create(tagged = marieke_sweater, tag = clothing)
    TagHanger.create(tagged = marieke_sweater, tag = cotton)
    TagHanger.create(tagged = marieke_sweater, tag = fleece)
    
    
    marieke_jacket = Product.create(
                                 owner=marieke_user, 
                                 name="Jacket",
                                 description="Short jacket in nice material that fits close to the body. The jacket can be zipped as you see both from above and below.",
                                 price_per_product=129.99,
                                 quantity=50, 
                                 )
    
    TagHanger.create(tagged = marieke_jacket, tag = clothing)

    hongs_chutney = Product.create(
                                 owner=hong_user, 
                                 name="Apple & Walnut Chutney",
                                 description="A full flavoured apple chutney with crushed walnuts and a little orange zest.",
                                 price_per_product=2.50,
                                 quantity=800, 
                                 )
    
    TagHanger.create(tagged = hongs_chutney, tag = food)
    TagHanger.create(tagged = hongs_chutney, tag = sweet)

    hongs_leek_mustard = Product.create(
                                 owner=hong_user, 
                                 name="Leek Mustard",
                                 description="Finely chopped leek are put into the mustard to create a hot strength.",
                                 price_per_product=1.00,
                                 quantity=3,                               
                                 )
  
    TagHanger.create(tagged = hongs_leek_mustard, tag = food)
    TagHanger.create(tagged = hongs_leek_mustard, tag = spicy)   
    

    hongs_lemon_dressing = Product.create(
                                 owner=hong_user, 
                                 name="Lemon & Dill Dressing",
                                 description="This is a fresh tasting dressing with the sharpness of lemons against lots of fresh sweet dill and seasoning. This may be poured over poached fish or on a salad of watercress, chicory and beetroot or even drizzle over pasta.",
                                 price_per_product=3.00,
                                 quantity=100,
                                 )
    
    Product.create(
        name="Bike",
        description="Shitty metal bike",
        price_per_product=350.00,
        quantity=6
    )
    
    Product.create(
        name="Water",
        description="Sour pieces of extremely wet water",
        price_per_product=1.00,
        quantity=1000000
    )
    
    Product.create(
        name="Norweigian Woodcutters Hands",
        description="Raw, not yet rotten, HUGE!",
        price_per_product=49.95,
        quantity=2
    )
    
    TagHanger.create(tagged = "Bike", tag = metal) 
    TagHanger.create(tagged = "Water", tag = sour) 
    TagHanger.create(tagged = "Water", tag = spicy) 
    

del_old_db()
populate_db()