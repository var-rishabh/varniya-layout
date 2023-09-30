estimates_html = '''
    <div style="width: 100%; height: 100%; position: relative; background-color: #fef7ed !important;">
    <img style="width: 215px; height: 64px; left: 77px; top: 662px; position: absolute" src="https://dev-apps-bucket.sgp1.digitaloceanspaces.com/admin-panel/varuns-signature.png" />
    <img style="width: 120px; height: 115px; left: 417px; top: 621px; position: absolute" src="https://dev-apps-bucket.sgp1.digitaloceanspaces.com/admin-panel/varniya-stamp.png" />
    <div style="width: 499px; left: 54px; top: 121px; position: absolute; color: #453638; font-size: 14px; font-family: Cinzel; font-weight: 700; word-wrap: break-word">A Clearly Good Price Estimation</div>
    <img style="width: 215px; height: 50.13px; left: 52px; top: 48.13px; position: absolute" src="https://dev-apps-bucket.sgp1.digitaloceanspaces.com/admin-panel/varniya-logo.png" />
    <div style="width: 488px; left: 54px; top: 170px; position: absolute"><span style="color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">Hello </span><span style="color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 700; word-wrap: break-word">{{ customer_name }}</span><span style="color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">,<br/><br/>Attached is an estimate for a </span><span style="color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 700; text-decoration: underline; word-wrap: break-word">{{ jewellery_name_type }}</span><span style="color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">, with their respective colour and clarity grades.</span></div>
    <div style="width: 250px; left: 54px; top: 536px; position: absolute; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">We request a 50% advance to process your order and give you an estimated delivery date.<br/><br/>You can expect your design to be custom made and delivered within 2 weeks of making an advance payment. Please allow some flexibility.</div>
    <img style="width: 149.10px; height: 150px; left: 63px; top: 275px; position: absolute" src={{ jewellery_image }} />
    <div style="left: 318px; top: 536px; position: absolute; color: black; font-size: 12px; font-family: Cormorant Garamond; font-weight: 700; word-wrap: break-word">Bank Details:  E.& O.E.</div>
    <div style="width: 120px; left: 464px; top: 81px; position: absolute; text-align: center; color: #453638; font-size: 14px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">{{ todays_date }}</div>
    <div style="width: 127px; height: 17px; left: 417px; top: 118px; position: absolute; text-align: right; color: #453638; font-size: 14px; font-family: Cormorant Garamond; font-weight: 700; word-wrap: break-word">{{ invoice number }}</div>
    <div style="width: 232px; left: 318px; top: 551px; position: absolute"><span style="color: black; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">UPI: </span><span style="color: black; font-size: 12px; font-family: Cormorant Garamond; font-weight: 700; word-wrap: break-word">varniyadiamonds@ybl</span><span style="color: black; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">    Name: WELLMO SERVICES (OPC) Pvt Ltd <br/>Branch: IndusInd Bank, Anna Nagar, Al Complex<br/>Account # 201003002675 <br/>IFSC : INDB0000046</span></div>
    <div style="width: 326px; height: 25px; left: 215px; top: 256px; position: absolute">
        <div style="width: 326px; height: 25px; left: 0px; top: 0px; position: absolute; background: #453638"></div>
        <div style="width: 67px; height: 25px; left: 23px; top: 0px; position: absolute; color: white; font-size: 12px; font-family: Cormorant Garamond; font-weight: 700; word-wrap: break-word">Details</div>
        <div style="width: 55px; height: 25px; left: 246px; top: 0px; position: absolute; text-align: center; color: white; font-size: 13px; font-family: Cormorant Garamond; font-weight: 700; word-wrap: break-word">Amount</div>
    </div>
    <div style="width: 67.01px; height: 0px; left: 307px; top: 622.01px; position: absolute; transform: rotate(-90deg); transform-origin: 0 0; border: 0.70px #453638 solid"></div>
    <div style="height: 113px; left: 238px; top: 287px; position: absolute">
        <div style="width: 478px; height: 30px; left: 0px; top: 0px; position: absolute">
            <div style="width: 200.33px; left: 0px; top: 0px; position: absolute; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">{{ metal_name }}<br> - {{ metal_weight }} grams @ {{ metal_price_per_gram }}/gram</div>
            <div style="width: 100px; left: 227px; top: 0px; position: absolute; text-align: right; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">{{ metal_price }}</div>
        </div>
        <div style="width: 400px; height: 30px; left: 0px; top: 46px; position: absolute">
            <div style="width: 190.64px; left: 0px; top: 0px; position: absolute; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">Center Diamond<br/> - {{ center_diamond_weight }} X {{ center_diamond_clarity_type }} - {{ center_diamond_carat }} Carat</div>
            <div style="width: 150px; left: 226px; top: 0px; position: absolute; text-align: right; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">{{ center_diamond_price }}</div>
        </div>
        <div style="width: 278px; height: 15px; left: 0px; top: 90px; position: absolute">
            <div style="width: 100px; left: 0px; top: 0px; position: absolute; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">Making Charges</div>
            <div style="width: 120px; left: 226px; top: 0px; position: absolute; text-align: right; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">{{ making_charges }}</div>
        </div>
        <div style="width: 278px; height: 15px; left: 0px; top: 105px; position: absolute">
            <div style="width: 140.03px; left: 0px; top: 0px; position: absolute; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">Addons</div>
            <div style="width: 140px; left: 227px; top: 0px; position: absolute; text-align: right; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">{{ certification_charges }}</div>
        </div>
        <div style="width: 278px; height: 15px; left: 0px; top: 120px; position: absolute">
            <div style="width: 80.45px; left: 0px; top: 0px; position: absolute; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">GST @ 3%</div>
            <div style="width: 120px; left: 227px; top: 0px; position: absolute; text-align: right; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">{{ gst_charges }}</div>
        </div>
    </div>
    <div style="width: 286.77px; height: 0px; left: 235px; top: 426px; position: absolute; border: 0.70px black solid"></div>
    <div style="width: 278px; height: 17px; left: 238px; top: 432px; position: absolute">
        <div style="width: 155.76px; left: 0px; top: 0px; position: absolute; color: #453638; font-size: 14px; font-family: Co{{rmorant Garamond; font-weight: 700; word-wrap: break-word">Estimated Total Amount</div>
        <div style="width: 130.19px; left: 221.81px; top: 0px; position: absolute; text-align: right; color: #453638; font-size: 14px; font-family: Cormorant Garamond; font-weight: 700; word-wrap: break-word">{{ estimated_total }}</div>
    </div>
</div>
'''

guesstimate_html = '''
<div style="width: 100%; height: 100%; position: relative; background: linear-gradient(0deg, #FEF7ED 0%, #FEF7ED 100%)">
    <img style="width: 215px; height: 64px; left: 77px; top: 662px; position: absolute" src="https://dev-apps-bucket.sgp1.digitaloceanspaces.com/admin-panel/varuns-signature.png" />
    <img style="width: 120px; height: 115px; left: 417px; top: 621px; position: absolute" src="https://dev-apps-bucket.sgp1.digitaloceanspaces.com/admin-panel/varniya-stamp.png" />
    <div style="width: 499px; left: 54px; top: 116px; position: absolute; color: #453638; font-size: 14px; font-family: Cinzel; font-weight: 700; word-wrap: break-word">A Clearly Good Price Estimation</div>
    <img style="width: 215px; height: 50.13px; left: 52px; top: 48.13px; position: absolute" src="https://dev-apps-bucket.sgp1.digitaloceanspaces.com/admin-panel/varniya-logo.png" />
    <div style="width: 488px; left: 54px; top: 170px; position: absolute"><span style="color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">Hello </span><span style="color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 700; word-wrap: break-word">{{ customer_name }}</span><span style="color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">,<br/><br/>Attached is an estimate for a </span><span style="color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 700; text-decoration: underline; word-wrap: break-word">{{ jewellery_name_type }}</span><span style="color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">, with their respective colour and clarity grades.</span></div>
    <div style="width: 250px; left: 52px; top: 536px; position: absolute; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">We request a 50% advance to process your order and give you an estimated delivery date.<br/><br/>You can expect your design to be custom made and delivered within 2 weeks of making an advance payment. Please allow some flexibility.</div>
    <img style="width: 149.10px; height: 150px; left: 63px; top: 266px; position: absolute" src={{ jewellery_image }} />
    <div style="width: 200px; left: 463px; top: 60px; position: absolute; text-align: center; color: #453638; font-size: 14px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">{{ todays_date }}</div>
    <div style="width: 312px; height: 25px; left: 216px; top: 253px; position: absolute">
        <div style="width: 312px; height: 25px; left: 0px; top: 0px; position: absolute; background: #453638"></div>
        <div style="width: 136.86px; height: 25px; left: 10px; top: 0px; position: absolute; color: white; font-size: 12px; font-family: Cormorant Garamond; font-weight: 700; word-wrap: break-word">Option 1 - {{ clarity_type_1_name }}</div>
        <div style="width: 54px; height: 25px; left: 246px; top: 0px; position: absolute; text-align: right; color: white; font-size: 13px; font-family: Cormorant Garamond; font-weight: 700; word-wrap: break-word">Amount</div>
    </div>
    <div style="width: 67.01px; height: 0px; left: 307px; top: 614.01px; position: absolute; transform: rotate(-90deg); transform-origin: 0 0; border: 0.70px #453638 solid"></div>
    <div style="width: 312px; height: 25px; left: 216px; top: 437px; position: absolute">
        <div style="width: 312px; height: 25px; left: 0px; top: 0px; position: absolute; background: #453638"></div>
        <div style="width: 134px; height: 25px; left: 11px; top: 0px; position: absolute; color: white; font-size: 12px; font-family: Cormorant Garamond; font-weight: 700; word-wrap: break-word">Option 2 - {{ clarity_type_2_name }}</div>
        <div style="width: 54px; height: 25px; left: 246px; top: 0px; position: absolute; text-align: right; color: white; font-size: 13px; font-family: Cormorant Garamond; font-weight: 700; word-wrap: break-word">{{ estimated_amount_for_clarity_type_2 }}</div>
    </div>
    <div style="width: 289px; height: 138.50px; left: 227px; top: 285px; position: absolute">
        <div style="width: 288.84px; height: 30px; left: 0.04px; top: 0px; position: absolute">
            <div style="width: 156.19px; left: 0px; top: 0px; position: absolute; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">{{ metal_name }}<br/> - {{ metal_details }}</div>
            <div style="width: 80.65px; left: 248.19px; top: 0px; position: absolute; text-align: right; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">{{ metal_price }}</div>
        </div>
        <div style="width: 288.96px; height: 15px; left: 0.04px; top: 98px; position: absolute">
            <div style="width: 52.44px; left: 0px; top: 0px; position: absolute; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">GST @ 3%</div>
            <div style="width: 38.53px; left: 250.43px; top: 0px; position: absolute; text-align: right; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">{{ gst_charges }}</div>
        </div>
        <div style="width: 288.84px; height: 15px; left: 0.04px; top: 64px; position: absolute">
            <div style="width: 82.37px; left: 0px; top: 0px; position: absolute; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">Making Charges</div>
            <div style="width: 38.51px; left: 250.33px; top: 0px; position: absolute; text-align: right; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">{{ making_charges }}</div>
        </div>
        <div style="width: 288.84px; height: 15px; left: 0.04px; top: 81px; position: absolute">
            <div style="width: 145.49px; left: 0px; top: 0px; position: absolute; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">Addons</div>
            <div style="width: 38.51px; left: 250.33px; top: 0px; position: absolute; text-align: right; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">0</div>
        </div>
        <div style="width: 288.84px; height: 30px; left: 0.04px; top: 32px; position: absolute">
            <div style="width: 131.58px; left: 0px; top: 0px; position: absolute; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">Center Diamond<br/> - {{ center_diamond_details }}</div>
            <div style="width: 48.14px; left: 240.70px; top: 0px; position: absolute; text-align: right; color: #453638; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">{{ center_diamond_price }}</div>
        </div>
        <div style="width: 286.77px; height: 0px; left: 1.08px; top: 117px; position: absolute; border: 0.70px black solid"></div>
        <div style="width: 289px; height: 17px; left: 0px; top: 121.50px; position: absolute">
            <div style="width: 161.92px; left: 0px; top: 0px; position: absolute; color: #453638; font-size: 14px; font-family: Cormorant Garamond; font-weight: 700; word-wrap: break-word">Estimated Total Amount</div>
            <div style="width: 58.41px; left: 230.58px; top: 0px; position: absolute; text-align: right; color: #453638; font-size: 14px; font-family: Cormorant Garamond; font-weight: 700; word-wrap: break-word">{{ estimated_amount_for_clarity_type_1 }}</div>
        </div>
    </div>
    <div style="width: 312px; height: 26px; left: 216px; top: 467px; position: absolute">
        <div style="width: 312px; height: 26px; left: 0px; top: 0px; position: absolute; background: #453638"></div>
        <div style="width: 52px; height: 26px; left: 248px; top: 0px; position: absolute; text-align: right; color: white; font-size: 13px; font-family: Cormorant Garamond; font-weight: 700; word-wrap: break-word">{{ estimated_amount_for_clarity_type_3 }}</div>
        <div style="width: 134px; height: 26px; left: 11px; top: 0px; position: absolute; color: white; font-size: 12px; font-family: Cormorant Garamond; font-weight: 700; word-wrap: break-word">Option 3 - {{ clarity_type_3_name }}</div>
    </div>
    <div style="left: 318px; top: 536px; position: absolute; color: black; font-size: 12px; font-family: Cormorant Garamond; font-weight: 700; word-wrap: break-word">Bank Details:  E.& O.E.</div>
    <div style="width: 232px; left: 318px; top: 551px; position: absolute"><span style="color: black; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">UPI: </span><span style="color: black; font-size: 12px; font-family: Cormorant Garamond; font-weight: 700; word-wrap: break-word">varniyadiamonds@ybl</span><span style="color: black; font-size: 12px; font-family: Cormorant Garamond; font-weight: 400; word-wrap: break-word">    Name: WELLMO SERVICES (OPC) Pvt Ltd <br/>Branch: IndusInd Bank, Anna Nagar, Al Complex<br/>Account # 201003002675 <br/>IFSC : INDB0000046</span></div>
</div>
'''
