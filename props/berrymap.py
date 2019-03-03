from props import berry
berry_dict={
    '樱子果': berry.Berry(show_name='樱子果',code='01'),
    '零余果': berry.Berry(show_name='零余果',code='02'),
}

berry_bag={
    1:[berry_dict['樱子果'],1],
}


berry_effect_for_NaturalGift={
    '01': (80,'fire'),
    '02': (80,'water'),
}