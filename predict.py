from model import train_model, predict
from config import model_path

if __name__ == '__main__':
    train_model.load_weights(model_path)
    sentence_list = [
        '如何演好自己的角色，请读《演员自我修养》《喜剧之王》周星驰崛起于穷困潦倒之中的独门秘笈',
        '《下半生留住你一直相爱》是商人醉猫写的网络小说连载于17k小说网',
        '个人简介梁信强，男，2010年广州亚运会中国澳门代表团成员',
        '李春英，女，汉族，1970年1月生，山东临清市人，大学，1992年7月参加工作，1999年6月加入中国共产党',
        '黄强，男，汉族，1961年2月生，广东廉江人，1985年11月加入中国共产党，1976年10月参加工作，中山大学哲学系中国哲学专业，在职研究生学历，哲学博士'
        '《狙击部队》是由江苏海润影视制作有限公司出品的电视剧，由赵浚凯执导，王珂、赵聪、刘鑫等主演',
        '查尔斯·阿兰基斯（Charles Aránguiz），1989年4月17日出生于智利圣地亚哥，智利职业足球运动员，司职中场，效力于德国足球甲级联赛勒沃库森足球俱乐部',
        '马志舟，1907年出生，陕西三原人，汉族，中国共产党，任红四团第一连连长，1933年逝世',
        '斑刺莺是雀形目、剌嘴莺科的一种动物，分布于澳大利亚和新西兰，包括澳大利亚、新西兰、塔斯马尼亚及其附近的岛屿',
        '伴随着春节的结束，又有一批新剧播出，包括张一山的《我的父亲我的兵》，左小青的《台湾往事》，还有《风光大嫁》等'
    ]
    for item in predict(sentence_list=sentence_list):
        print("-----------")
        sent, result_list = item
        print("原句: {sent}".format(sent=sent))
        print("三元组:")
        for item in result_list:
            s = item['subject']
            p = item['predicate']
            o = item['object']
            print((s, p, o))
