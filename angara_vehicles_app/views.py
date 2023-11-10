from django.shortcuts import render

# Create your views here.

descrips = [
            "В августе 2018 года было сообщено, что первая товарная партия титановых шаробаллонов (ТШБ) для ракет-носителей «Ангара» отправлена с Воронежского механического завода (ВМЗ) в ПО «Полёт». Это первый комплект ТШБ российского производства: до 2014 года для российских ракет-носителей их поставлял завод «Южмаш» (Украина)",
            "В качестве верхней ступени предусмотрено применение разгонных блоков: «Бриз-КМ», «Бриз-М», кислородно-водородный среднего класса (КВСК) и кислородно-водородный тяжёлого класса (КВТК)",
            "«Бисер-6» предназначен для управления движением и бортовыми системами, а также для контроля полёта и формирования телеметрической информации. При решении задач навигации и наведения с помощью «Бисера-6» выполняются арифметические и логические операции, а также операции обмена информацией с внешними абонентами. В компьютере «Бисер-6» сосредоточены средства контроля и диагностики различных устройств системы управления. «Бисер-6» является программно-совместимым продолжением хорошо зарекомендовавшей себя БЦВМ «Бисер-3». Однако у «Бисера-6» значительно улучшены габаритно-весовые, энергетические характеристики и надёжность. Ещё одна особенность машины «Бисер-6»: элементная база исключительно российского производства и повышенная стойкость к воздействию специальных факторов. Для парирования сбоев при воздействии специальных факторов применяются дополнительные средства функциональной защиты",
            "Носитель тяжелого класса «Ангара-5А» имеет первую ступень, образованную из пяти блоков на основе универсального ракетного модуля. Пять двигателей первой ступени запускаются при старте ракеты одновременно, но впоследствии двигатель центрального блока дросселируется до 30% тяги и к моменту опорожнения боковых модулей сохраняет достаточные запасы топлива для продолжения полета. Опорожнившиеся боковые модули сбрасываются, а центральный модуль переводится на режим полной тяги. Предельной по количеству УРМ-1 может быть РН «Ангара А5».Универсальный ракетный модуль представляет собой законченную конструкцию, состоящую из баков окислителя и горючего, соединенных проставкой, и двигательного отсека. УРМ-1 оснащается жидкостным реактивным двигателем РД-191 (разработан НПО «Энергомаш»), УРМ-2 – двигателем РД-0124А (разработан КБХА). Двигатель впервые в России был спроектирован по безгенераторной схеме, обеспечивающей высокую надежность, особенно при многократных включениях. В двигателе применены раздельные турбонасосные агрегаты кислорода и водорода, причем рабочая частота вращения ротора ТНАГ-123 тыс.об/мин",
            "В основу семейства носителей «Ангара» положен универсальный ракетный модуль (УРМ). В его состав входит блок <b>баков окислителя</b>, <b>горючего</b> и <b>двигатель РД-191</b>. Модуль выполнен по схеме «моноблок» с несущими баками. <br>Однокамерный двигатель РД-191, создаваемый в НПО «Энергомаш», работает на компонентах керосин/жидкий кислород. Этот двигатель является вариантом четырехкамерных двигателей РД-170 и РД-171, устанавливавшихся на первых ступенях PH «Энергия» и PH «Зенит-2» соответственно, и двухкамерного двигателя РД-180, созданного для PH «Атлас». Его тяга у земли 1923 кН, в пустоте - 2086 кН, удельный импульс тяги на Земле - 3048 Н*с/кг, в пустоте -3306 Н*с/кг. Для обеспечения управления ракетой-носителем в полете двигатель закрепляется в карданном подвесе. Один такой универсальный ракетный модуль является первой ступенью двух типов носителей легкого класса, создаваемых в рамках программы «Ангара»",
            "Задача головных обтекателей ракет-носителей – на момент старта и до вывода в космическое пространство – это защита космического аппарата от всех внешних факторов. Максимальной температурой головного обтекателя считается 175 градусов Цельсия по поверхности",
            "В качестве второй ступени рассматривается либо ступень на компонентах кислород-керосин, аналогичная применяемой на носителе «Ангара-1.2», но с увеличенным запасом компонентов топлива, либо универсальный кислородно-водородный блок («УКВБ»), характеристики которого сохраняются такими же, как «УКВБ» для носителя «Протон-М2»"
           ]

def GetData(id):
    options = {'data': {
        'vars': [
            {
                'id': 1,
                'title': 'Титановый шаробалонн',
                'category': 'Дополнительные запчасти',
                'description': descrips[0],
                'image': 'image/титановые_шаробаллоны.png',
            },
            {
                'id': 2,
                'title': 'Разгонный блок "Бриз-М"',
                'category': 'Разгонные блоки',
                'description': descrips[1],
                'image': 'image/разгонный_блок_бриз-м.png',
            },
            {
                'id': 3,
                'title': 'Центральная вычислительная машина "Бисер-6"',
                'category': 'Электроника',
                'description': descrips[2],
                'image': 'image/цвм.png',
            },
            {
                'id': 4,
                'title': 'Боковой (универсальный) ракетный модуль - урм 1 (составная часть 1-ой ступени)',
                'category': 'Универсальные ракетные модули',
                'description': descrips[3],
                'image': 'image/урм-1.png',
            },
            {
                'id': 5,
                'title': 'Центральный ракетный модуль (составная часть 1-ой ступени)',
                'category': 'Универсальные ракетные модули',
                'description': descrips[4],
                'image': 'image/центральный_блок.jpeg',
            },
            {
                'id': 6,
                'title': 'Головной обтекатель',
                'category': 'Головные модули',
                'description': descrips[5],
                'image': 'image/головной обтекатель.jpg',
            },
            {
                'id': 7,
                'title': 'Вторая ступень - универсальный ракетный модуль 2 (урм 2)',
                'category': 'Универсальные ракетные модули',
                'description': descrips[6],
                'image': 'image/вторая_ступень_1.png',
            },
        ]
    }}
    if id != 0:
        return options['data']['vars'][id - 1]
    else:
        return options['data']


def GetOptions(request):
    input_text = request.GET.get("rocketcomp")
    print(input_text)
    if input_text:
        options = GetData(0)
        print(options)
        filtered_options = [var for var in options['vars'] if input_text.lower() in var['category'].lower()]
        print(filtered_options)
        context = {'vars': filtered_options, 'find': input_text}
        print(context['find'])
        return render(request, 'main_page.html', context)
    else:
        return render(request, 'main_page.html', GetData(0))

def GetOption(request, id):
    return render(request, 'rocket_page.html', GetData(id))