import ujson

modelData = open("model.json", encoding='utf-8')
brandData = open("brand.json", encoding='utf-8')
# 转换为python对象
modelList = ujson.load(modelData)
brandList = ujson.load(brandData)

allData = list()
for brand in brandList:
    count = 0
    brand_ls = list()
    model_ls = list()
    for m in modelList:
        if brand == m['BRAND_EN']:
            brand_ls.append(m)
            if m['MODEL'] == "no_model":
                continue
            model_ls.append(m['MODEL'])
    brands = dict(
            serial=len(brand_ls),
            brand=brand,
            model=model_ls
        )

    allData.append(brands)
print(ujson.dumps(allData))
