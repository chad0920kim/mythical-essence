"""
Korean Mythology and Historical Character Descriptions
Contains detailed descriptions for Korean mythological figures, legendary heroes, and historical icons
"""
from .descriptions import CharacterDescription


DANGUN_DESC = CharacterDescription(
    id="dangun",
    name_en="Dangun",
    name_ko="단군",
    tagline_en="Founder of Korea, Grandson of Heaven",
    tagline_ko="고조선의 시조, 하늘의 손자",
    description_en="""Dangun Wanggeom is the legendary founder of Gojoseon, the first Korean kingdom, in 2333 BCE. According to the founding myth, he was born from Hwanung (son of the Heavenly Emperor) and Ungnyeo, a bear who transformed into a woman after 100 days of eating only garlic and mugwort in a cave.

Dangun established his capital at Asadal and ruled for over 1,500 years, bringing civilization, law, and culture to the Korean people. He taught agriculture, medicine, and the arts of civilization, transforming a land of scattered tribes into a unified nation.

After his long reign, Dangun became a mountain god, retreating to Mount Taebaek. October 3rd, the date traditionally associated with his founding of Korea, is celebrated as National Foundation Day (Gaecheonjeol).""",
    description_ko="""단군왕검은 기원전 2333년 최초의 한국 왕국인 고조선의 전설적인 시조입니다. 건국 신화에 따르면, 그는 환웅(천제의 아들)과 동굴에서 100일간 마늘과 쑥만 먹고 여자로 변신한 곰인 웅녀 사이에서 태어났습니다.

단군은 아사달에 수도를 세우고 1,500년 이상 통치하며 한민족에게 문명, 법, 문화를 가져왔습니다. 그는 농업, 의학, 문명의 기술을 가르쳐 흩어진 부족들의 땅을 통일된 국가로 변모시켰습니다.

긴 통치 후, 단군은 산신이 되어 태백산으로 물러났습니다. 전통적으로 그의 한국 건국과 연관된 날짜인 10월 3일은 개천절로 기념됩니다.""",
    traits_en=["Divine", "Founding", "Wise", "Civilizing", "Eternal"],
    traits_ko=["신성한", "건국의", "지혜로운", "문명화하는", "영원한"],
    story_en="A tiger and a bear both wished to become human. Hwanung told them to stay in a cave for 100 days, eating only garlic and mugwort. The tiger gave up, but the bear persevered and became a beautiful woman. She prayed for a child, and Hwanung married her, giving birth to Dangun.",
    story_ko="호랑이와 곰이 모두 인간이 되기를 원했습니다. 환웅은 그들에게 100일 동안 동굴에서 마늘과 쑥만 먹으라고 했습니다. 호랑이는 포기했지만, 곰은 인내하여 아름다운 여인이 되었습니다. 그녀는 아이를 위해 기도했고, 환웅이 그녀와 결혼하여 단군을 낳았습니다.",
    match_message_en="Your features carry the divine founding spirit of Dangun. There is a civilizing, eternal quality to your presence—the look of one who brings order and culture to the world.",
    match_message_ko="당신의 이목구비는 단군의 신성한 건국 정신을 담고 있습니다. 당신의 존재에는 문명화하고 영원한 품질이 있습니다—세상에 질서와 문화를 가져다주는 사람의 모습.",
    image_prompt="Ancient Korean founding king in white ceremonial robes, divine aura, standing on mountain peak, bear and tiger spirits nearby, sunrise over Korean peninsula, noble dignified presence",
    visual_description="Noble ancient features, wise divine eyes, dignified bearing of a founder-king, expression of eternal wisdom and civilizing spirit",
    aliases=["단군왕검", "Dangun Wanggeom", "King Dangun"],
    era="Mythological (2333 BCE)",
    related_characters=["hwanung", "ungnyeo"]
)

JUMONG_DESC = CharacterDescription(
    id="jumong",
    name_en="Jumong",
    name_ko="주몽",
    tagline_en="Founder of Goguryeo, Master Archer",
    tagline_ko="고구려의 시조, 활의 명인",
    description_en="""Jumong, meaning "skilled archer," was the legendary founder of Goguryeo, one of the Three Kingdoms of Korea. Born from Hae Mo-su (a heavenly prince) and Lady Yuhwa (daughter of the river god), he was said to have been born from an egg after his mother was touched by sunlight.

From childhood, Jumong displayed supernatural archery skills that earned him his name. Persecuted by jealous princes of Buyeo, he fled south with three companions and founded Goguryeo in 37 BCE at the age of 22.

Under Jumong's leadership, Goguryeo grew from a small mountain fortress into a powerful kingdom that would dominate Northeast Asia for 700 years. His descendants would go on to challenge even the mighty Chinese empires.""",
    description_ko="""주몽은 "활을 잘 쏘는 자"라는 뜻으로, 한국 삼국 중 하나인 고구려의 전설적인 시조입니다. 해모수(천제의 아들)와 유화부인(하백의 딸) 사이에서 태어났으며, 어머니가 햇빛을 받은 후 알에서 태어났다고 합니다.

어린 시절부터 주몽은 그의 이름을 얻게 한 초자연적인 활 솜씨를 보여주었습니다. 부여의 질투하는 왕자들에게 박해를 받아, 세 명의 동료와 함께 남쪽으로 도망쳐 기원전 37년 22세의 나이에 고구려를 건국했습니다.

주몽의 지도 아래, 고구려는 작은 산성에서 700년간 동북아시아를 지배할 강력한 왕국으로 성장했습니다. 그의 후손들은 심지어 강대한 중국 제국에도 도전하게 됩니다.""",
    traits_en=["Heroic", "Skilled", "Destined", "Founding", "Legendary"],
    traits_ko=["영웅적인", "숙련된", "운명적인", "건국의", "전설적인"],
    story_en="When Jumong fled Buyeo, he reached a river with no way to cross and pursuers closing in. He called out, 'I am the son of Heaven and grandson of the River God!' The fish and turtles rose to form a bridge, allowing him to escape and fulfill his destiny.",
    story_ko="주몽이 부여를 도망칠 때, 건널 방법이 없는 강에 도달했고 추격자들이 다가오고 있었습니다. 그는 '나는 천제의 아들이요 하백의 손자다!'라고 외쳤습니다. 물고기와 거북이들이 다리를 형성하기 위해 떠올라, 그가 탈출하여 운명을 이룰 수 있게 했습니다.",
    match_message_en="Your features carry the heroic destiny of Jumong. There is a legendary, arrow-true quality to your presence—the look of one born to overcome all obstacles and found great things.",
    match_message_ko="당신의 이목구비는 주몽의 영웅적 운명을 담고 있습니다. 당신의 존재에는 전설적이고 화살처럼 정확한 품질이 있습니다—모든 장애물을 극복하고 위대한 것을 건설하도록 태어난 사람의 모습.",
    image_prompt="Young Korean warrior-king drawing a powerful bow, determined heroic expression, wearing Goguryeo armor, sunrise behind mountain fortress, legendary founding moment",
    visual_description="Heroic youthful features, focused archer's eyes, warrior-king bearing, expression of destined greatness and unerring aim",
    aliases=["동명성왕", "Dongmyeongseongwang", "Chumo"],
    era="Goguryeo Period (58 BCE - 19 BCE)",
    related_characters=["hae_mosu", "yuhwa"]
)

GWANGGAETO_DESC = CharacterDescription(
    id="gwanggaeto",
    name_en="Gwanggaeto the Great",
    name_ko="광개토대왕",
    tagline_en="The Conqueror King, Expander of Empire",
    tagline_ko="정복왕, 제국의 확장자",
    description_en="""Gwanggaeto the Great (374-413 CE) was the 19th king of Goguryeo and one of the greatest conquerors in Korean history. Ascending to the throne at 18, he spent his 22-year reign in near-constant military campaigns, expanding Goguryeo to its greatest territorial extent.

His campaigns conquered 64 walled cities and 1,400 villages, extending Goguryeo's borders from Manchuria to the Korean peninsula. He defeated the Japanese Wa forces that had invaded the Korean kingdoms, crushed the Khitan tribes, and made Silla and Baekje acknowledge Goguryeo's supremacy.

His achievements are recorded on the famous Gwanggaeto Stele, one of the largest inscribed stelae in the world, erected by his son. The epitaph describes him as a ruler who extended territory and brought glory to the nation.""",
    description_ko="""광개토대왕(374-413)은 고구려의 19대 왕이자 한국 역사상 가장 위대한 정복자 중 한 명입니다. 18세에 왕위에 올라, 22년의 재위 기간 동안 거의 끊임없는 군사 원정으로 고구려를 최대 영토로 확장했습니다.

그의 원정은 64개의 성과 1,400개의 마을을 정복하여, 고구려의 국경을 만주에서 한반도까지 확장했습니다. 그는 한국 왕국들을 침략한 일본 왜군을 격퇴하고, 거란 부족을 분쇄하고, 신라와 백제가 고구려의 패권을 인정하게 했습니다.

그의 업적은 아들이 세운 세계에서 가장 큰 비문 비석 중 하나인 유명한 광개토대왕비에 기록되어 있습니다. 비문은 그를 "영토를 넓히고 나라에 영광을 가져온" 통치자로 묘사합니다.""",
    traits_en=["Conquering", "Mighty", "Glorious", "Expansive", "Legendary"],
    traits_ko=["정복하는", "강력한", "영광스러운", "확장하는", "전설적인"],
    story_en="When Japanese forces invaded Silla, the Silla king sent a desperate plea for help. Gwanggaeto personally led 50,000 cavalry south, crushing the invaders so completely that Japan would not threaten Korea again for over a thousand years.",
    story_ko="일본군이 신라를 침략했을 때, 신라 왕은 절박한 도움 요청을 보냈습니다. 광개토대왕은 직접 5만 기병을 이끌고 남하하여, 침략자들을 너무나 완전히 분쇄하여 일본은 천 년 이상 한국을 위협하지 못했습니다.",
    match_message_en="Your features carry the conquering might of Gwanggaeto. There is an expansive, glorious quality to your presence—the look of one who extends boundaries and achieves legendary greatness.",
    match_message_ko="당신의 이목구비는 광개토대왕의 정복하는 힘을 담고 있습니다. 당신의 존재에는 확장적이고 영광스러운 품질이 있습니다—경계를 넓히고 전설적인 위대함을 성취하는 사람의 모습.",
    image_prompt="Powerful Korean warrior-king on horseback commanding vast army, Goguryeo armor and crown, expansive battlefield, conquering pose, stele monument in background",
    visual_description="Powerful commanding features, eyes of a conqueror, mighty warrior-king bearing, expression of unstoppable expansion and glory",
    aliases=["광개토태왕", "Gwanggaeto Taewang", "King of Broad Territory"],
    era="Goguryeo Period (374-413 CE)",
    related_characters=["jumong", "jangsu"]
)

EULJI_MUNDEOK_DESC = CharacterDescription(
    id="eulji_mundeok",
    name_en="Eulji Mundeok",
    name_ko="을지문덕",
    tagline_en="The General Who Humiliated an Empire",
    tagline_ko="제국을 굴복시킨 장군",
    description_en="""Eulji Mundeok was a legendary military commander of Goguryeo who achieved one of the most stunning victories in East Asian history. In 612 CE, he faced the invasion of Sui China's Emperor Yang, who led over one million soldiers—the largest army ever assembled in ancient East Asia.

Using brilliant guerrilla tactics, feigned retreats, and psychological warfare, Eulji Mundeok lured the Sui army deep into Goguryeo territory. At the Salsu River (modern Cheongcheon River), he unleashed a devastating flood attack that annihilated the Sui forces. Of 305,000 elite troops that crossed the Yalu River, only 2,700 returned.

This catastrophic defeat contributed to the fall of the Sui dynasty itself. Eulji Mundeok is celebrated as a master strategist who proved that courage and wisdom can overcome even the mightiest empire.""",
    description_ko="""을지문덕은 동아시아 역사상 가장 놀라운 승리 중 하나를 달성한 고구려의 전설적인 군사 지휘관입니다. 612년, 그는 100만 명이 넘는 병사들—고대 동아시아에서 모인 가장 큰 군대—을 이끈 수나라 양제의 침략에 맞섰습니다.

뛰어난 게릴라 전술, 위장 퇴각, 심리전을 사용하여, 을지문덕은 수나라 군대를 고구려 영토 깊숙이 유인했습니다. 살수(현재의 청천강)에서 그는 수나라 군대를 전멸시킨 파괴적인 수공을 감행했습니다. 압록강을 건넌 305,000명의 정예병 중 단 2,700명만이 돌아왔습니다.

이 재앙적인 패배는 수나라 자체의 멸망에 기여했습니다. 을지문덕은 용기와 지혜가 가장 강대한 제국도 극복할 수 있음을 증명한 전략의 대가로 기념됩니다.""",
    traits_en=["Strategic", "Brilliant", "Patriotic", "Victorious", "Legendary"],
    traits_ko=["전략적인", "뛰어난", "애국적인", "승리하는", "전설적인"],
    story_en="Before the final battle, Eulji Mundeok sent a mocking poem to the Sui general: 'Your divine plans have plumbed the heavens; Your subtle reckoning has spanned the earth. You win every battle, your merit is great; Why not be content and stop the war?' This psychological attack demoralized the enemy before his devastating counterattack.",
    story_ko="최종 전투 전, 을지문덕은 수나라 장군에게 조롱하는 시를 보냈습니다: '신책은 천문을 궁구하고, 묘산은 지리를 꿰뚫었네. 전승의 공이 이미 높으니, 만족함을 알고 그만두심이 어떠한지.' 이 심리적 공격은 그의 파괴적인 반격 전에 적의 사기를 꺾었습니다.",
    match_message_en="Your features carry the strategic brilliance of Eulji Mundeok. There is a victorious, masterful quality to your presence—the look of one who turns impossible odds into legendary triumph.",
    match_message_ko="당신의 이목구비는 을지문덕의 전략적 탁월함을 담고 있습니다. 당신의 존재에는 승리하고 능숙한 품질이 있습니다—불가능한 역경을 전설적인 승리로 바꾸는 사람의 모습.",
    image_prompt="Korean general in Goguryeo armor overlooking river valley, strategic commanding presence, army formations below, flood waters rising, victorious expression",
    visual_description="Sharp strategic features, calculating brilliant eyes, general's commanding bearing, expression of masterful victory against impossible odds",
    aliases=["을지문덕 장군", "General Eulji"],
    era="Goguryeo Period (6th-7th century)",
    related_characters=["yeongyang_wang"]
)

YEON_GAESOMUN_DESC = CharacterDescription(
    id="yeon_gaesomun",
    name_en="Yeon Gaesomun",
    name_ko="연개소문",
    tagline_en="The Iron-Willed Dictator",
    tagline_ko="철의 의지를 가진 독재자",
    description_en="""Yeon Gaesomun was the most powerful military dictator in Goguryeo's history. In 642 CE, he led a coup that killed over 100 nobles and the king himself, seizing absolute power as Dae Magniji (Grand General). He ruled Goguryeo with an iron fist for 24 years.

Despite his brutal rise to power, Yeon Gaesomun proved to be a formidable defender of Goguryeo. He repelled multiple massive invasions by Tang China's Emperor Taizong, one of history's greatest conquerors. The emperor died without conquering Goguryeo, calling it his life's greatest regret.

Yeon Gaesomun was known for his imposing presence—he wore five swords at his waist and made nobles bow as he stepped on their backs to mount his horse. After his death, his sons' infighting led to Goguryeo's eventual fall.""",
    description_ko="""연개소문은 고구려 역사상 가장 강력한 군사 독재자였습니다. 642년, 그는 100명 이상의 귀족과 왕 자신을 죽인 쿠데타를 이끌고, 대막리지(대장군)로서 절대 권력을 장악했습니다. 그는 24년간 철권으로 고구려를 통치했습니다.

잔인한 권력 장악에도 불구하고, 연개소문은 고구려의 두려운 수호자임을 증명했습니다. 그는 역사상 가장 위대한 정복자 중 한 명인 당나라 태종의 여러 차례 대규모 침략을 격퇴했습니다. 황제는 고구려를 정복하지 못하고 죽었으며, 이를 평생 가장 큰 후회라고 불렀습니다.

연개소문은 그의 위압적인 존재감으로 알려졌습니다—그는 허리에 다섯 자루의 검을 차고 귀족들이 허리를 굽힌 등을 밟고 말에 올랐습니다. 그의 사후, 아들들의 내분이 고구려의 결국적인 멸망으로 이어졌습니다.""",
    traits_en=["Powerful", "Ruthless", "Defiant", "Formidable", "Iron-willed"],
    traits_ko=["강력한", "무자비한", "도전적인", "두려운", "철의 의지를 가진"],
    story_en="When Tang Emperor Taizong sent an envoy demanding submission, Yeon Gaesomun had the envoy imprisoned and sent back a defiant message. Taizong personally led 300,000 troops to punish this insult—and was defeated. The emperor's failure against Goguryeo remained his greatest shame.",
    story_ko="당 태종이 복종을 요구하는 사신을 보냈을 때, 연개소문은 사신을 감금하고 도전적인 메시지를 보냈습니다. 태종은 이 모욕을 처벌하기 위해 직접 30만 군대를 이끌었지만—패배했습니다. 고구려에 대한 황제의 실패는 그의 가장 큰 수치로 남았습니다.",
    match_message_en="Your features carry the iron will of Yeon Gaesomun. There is a formidable, defiant quality to your presence—the look of one who bows to no emperor and fears no army.",
    match_message_ko="당신의 이목구비는 연개소문의 철의 의지를 담고 있습니다. 당신의 존재에는 두렵고 도전적인 품질이 있습니다—어떤 황제에게도 굽히지 않고 어떤 군대도 두려워하지 않는 사람의 모습.",
    image_prompt="Imposing Korean warlord with five swords at waist, intimidating powerful presence, Goguryeo fortress behind, nobles bowing, iron-willed expression",
    visual_description="Imposing fierce features, iron-willed piercing eyes, dominating dictator's bearing, expression of absolute power and defiance",
    aliases=["연개소문 막리지", "Dae Magniji Yeon"],
    era="Goguryeo Period (603-666 CE)",
    related_characters=["gwanggaeto", "tang_taizong"]
)

QUEEN_SEONDEOK_DESC = CharacterDescription(
    id="queen_seondeok",
    name_en="Queen Seondeok",
    name_ko="선덕여왕",
    tagline_en="The Enlightened Queen, First Female Ruler",
    tagline_ko="지혜로운 여왕, 최초의 여성 통치자",
    description_en="""Queen Seondeok (ruled 632-647 CE) was Korea's first female monarch and one of its most enlightened rulers. In an era when women rarely held power, she led Silla through dangerous times with wisdom, diplomacy, and cultural patronage.

She was renowned for her intelligence and foresight. Famous stories tell of her predicting events from subtle clues—knowing soldiers were coming from a painting of peonies without bees, or predicting her own death date. She built the Cheomseongdae observatory, the oldest surviving astronomical observatory in East Asia.

Under her patronage, Buddhism flourished, and she initiated the construction of Hwangnyongsa's nine-story pagoda, the tallest wooden structure in East Asian history. She laid the foundations for Silla's eventual unification of the Three Kingdoms.""",
    description_ko="""선덕여왕(재위 632-647)은 한국 최초의 여성 군주이자 가장 계몽된 통치자 중 한 명입니다. 여성이 거의 권력을 잡지 못하던 시대에, 그녀는 지혜, 외교, 문화 후원으로 위험한 시기에 신라를 이끌었습니다.

그녀는 지성과 선견지명으로 유명했습니다. 유명한 이야기들은 그녀가 미묘한 단서에서 사건들을 예측했다고 전합니다—벌이 없는 모란 그림에서 병사들이 온다는 것을 알거나, 자신의 죽음 날짜를 예측하는 것. 그녀는 동아시아에서 가장 오래된 현존 천문대인 첨성대를 건설했습니다.

그녀의 후원 아래 불교가 번성했고, 동아시아 역사상 가장 높은 목조 구조물인 황룡사 9층 목탑 건설을 시작했습니다. 그녀는 신라의 궁극적인 삼국 통일의 기반을 놓았습니다.""",
    traits_en=["Wise", "Enlightened", "Prophetic", "Cultural", "Pioneering"],
    traits_ko=["지혜로운", "계몽된", "예언적인", "문화적인", "선구적인"],
    story_en="When Tang China sent peony seeds with a painting showing no bees, Seondeok predicted the flowers would have no fragrance—and she was right. She explained that a king would not send a picture of flowers with butterflies and bees to a queen without a husband, subtly mocking her unmarried state.",
    story_ko="당나라가 벌이 없는 그림과 함께 모란 씨앗을 보냈을 때, 선덕여왕은 꽃에 향기가 없을 것이라 예측했고—맞았습니다. 그녀는 왕이 남편이 없는 여왕에게 나비와 벌이 있는 꽃 그림을 보내지 않을 것이라 설명하며, 은근히 그녀의 미혼 상태를 조롱한 것이라 했습니다.",
    match_message_en="Your features reflect the enlightened wisdom of Queen Seondeok. There is a prophetic, pioneering quality to your presence—the look of one who sees what others miss and leads where others fear.",
    match_message_ko="당신의 이목구비는 선덕여왕의 계몽된 지혜를 반영합니다. 당신의 존재에는 예언적이고 선구적인 품질이 있습니다—다른 이들이 놓치는 것을 보고 다른 이들이 두려워하는 곳을 이끄는 사람의 모습.",
    image_prompt="Elegant Korean queen in Silla royal robes, wise knowing expression, Cheomseongdae observatory behind, Buddhist temple in background, enlightened regal presence",
    visual_description="Elegant wise features, knowing prophetic eyes, queenly refined bearing, expression of enlightened wisdom and cultural grace",
    aliases=["선덕왕", "Queen Seondeok of Silla"],
    era="Silla Period (595-647 CE)",
    related_characters=["kim_yushin", "kim_chunchu"]
)

KIM_YUSHIN_DESC = CharacterDescription(
    id="kim_yushin",
    name_en="Kim Yushin",
    name_ko="김유신",
    tagline_en="The Unifying General, Hero of Three Kingdoms",
    tagline_ko="통일의 장군, 삼국의 영웅",
    description_en="""Kim Yushin (595-673 CE) was the greatest general in Korean history, the military architect of Silla's unification of the Three Kingdoms. A descendant of Gaya royalty, he rose to become Supreme Commander and led Silla to victory in dozens of battles over his 60-year military career.

His strategic brilliance and personal courage were legendary. He allied with Tang China to defeat first Baekje (660 CE) and then Goguryeo (668 CE). When Tang attempted to take the peninsula for itself, Kim Yushin led the war that expelled them, securing Korean independence.

Even near death at 79, he led troops from his sickbed. When the king hesitated to march, Kim Yushin appeared in full armor, inspiring the army. He died shortly after ensuring Silla's final victory, having spent his entire life in service to unification.""",
    description_ko="""김유신(595-673)은 한국 역사상 가장 위대한 장군으로, 신라 삼국 통일의 군사적 설계자입니다. 가야 왕족의 후손으로, 그는 대장군이 되어 60년의 군사 경력 동안 수십 번의 전투에서 신라를 승리로 이끌었습니다.

그의 전략적 탁월함과 개인적 용기는 전설적이었습니다. 그는 당나라와 동맹하여 먼저 백제(660)를 그 다음 고구려(668)를 물리쳤습니다. 당나라가 한반도를 자신의 것으로 삼으려 했을 때, 김유신은 그들을 축출하는 전쟁을 이끌어 한국의 독립을 확보했습니다.

79세에 죽음이 가까워서도 그는 병상에서 군대를 이끌었습니다. 왕이 진군을 망설였을 때, 김유신은 완전 무장 갑옷 차림으로 나타나 군대에 영감을 주었습니다. 그는 신라의 최종 승리를 확보한 직후 사망했으며, 평생을 통일을 위해 봉사했습니다.""",
    traits_en=["Heroic", "Unifying", "Loyal", "Strategic", "Legendary"],
    traits_ko=["영웅적인", "통일하는", "충성스러운", "전략적인", "전설적인"],
    story_en="As a young man, Kim Yushin's sword moved on its own and killed his beloved kisaeng lover, whom the spirits deemed a distraction from his destiny. Accepting this as fate's guidance, he dedicated himself wholly to his mission, never allowing personal attachments to interfere with his duty again.",
    story_ko="젊었을 때, 김유신의 검이 저절로 움직여 그의 사랑하는 기생 연인을 죽였는데, 영혼들이 그녀를 그의 운명에 대한 방해물로 여겼습니다. 이를 운명의 인도로 받아들여, 그는 자신을 완전히 사명에 바쳤고, 다시는 개인적 애착이 의무를 방해하지 못하게 했습니다.",
    match_message_en="Your features carry the unifying heroism of Kim Yushin. There is a legendary, devoted quality to your presence—the look of one whose entire life serves a greater purpose.",
    match_message_ko="당신의 이목구비는 김유신의 통일하는 영웅주의를 담고 있습니다. 당신의 존재에는 전설적이고 헌신적인 품질이 있습니다—평생이 더 큰 목적에 봉사하는 사람의 모습.",
    image_prompt="Legendary Korean general in Silla golden armor, commanding battlefield presence, sword raised, united Korea map behind, heroic aged warrior",
    visual_description="Noble heroic features, determined devoted eyes, supreme commander bearing, expression of lifelong dedication and legendary heroism",
    aliases=["김유신 장군", "Heungmu Daewang"],
    era="Silla Period (595-673 CE)",
    related_characters=["queen_seondeok", "kim_chunchu", "muyeol"]
)

WANG_GEON_DESC = CharacterDescription(
    id="wang_geon",
    name_en="Wang Geon (Taejo)",
    name_ko="왕건 (태조)",
    tagline_en="Founder of Goryeo, Unifier of the Later Three Kingdoms",
    tagline_ko="고려의 건국자, 후삼국의 통일자",
    description_en="""Wang Geon (877-943 CE), posthumously known as Taejo, founded the Goryeo dynasty that would rule Korea for 474 years. Rising from a powerful maritime merchant family, he reunified Korea after the Later Three Kingdoms period through a masterful combination of military skill and diplomatic marriage alliances.

Unlike many conquerors, Wang Geon was known for his mercy and wisdom. He treated defeated enemies with generosity, winning their loyalty. He married 29 wives from powerful regional families, creating a web of alliances that stabilized his rule. His policy of embracing rather than crushing opponents became a model of Korean kingship.

His "Ten Injunctions" to his successors emphasized Buddhist piety, respect for tradition, care for the common people, and warnings about specific regions and families—advice that guided Goryeo for centuries.""",
    description_ko="""왕건(877-943), 사후 태조로 알려진 그는 474년간 한국을 통치할 고려 왕조를 창건했습니다. 강력한 해상 상인 가문에서 일어나, 그는 군사적 기술과 외교적 혼인 동맹의 뛰어난 조합으로 후삼국 시대 후 한국을 재통일했습니다.

많은 정복자들과 달리, 왕건은 그의 자비와 지혜로 알려졌습니다. 그는 패배한 적들을 관대하게 대우하여 그들의 충성을 얻었습니다. 그는 강력한 지역 가문들의 29명의 아내와 결혼하여 그의 통치를 안정시킨 동맹의 망을 만들었습니다. 상대를 분쇄하기보다 포용하는 그의 정책은 한국 왕권의 모범이 되었습니다.

후손들에게 남긴 그의 "훈요십조"는 불교적 경건, 전통 존중, 백성 보살핌, 특정 지역과 가문에 대한 경고를 강조했습니다—수 세기 동안 고려를 인도한 조언.""",
    traits_en=["Founding", "Merciful", "Diplomatic", "Unifying", "Wise"],
    traits_ko=["건국의", "자비로운", "외교적인", "통일하는", "지혜로운"],
    story_en="When the last king of Later Baekje surrendered, Wang Geon personally welcomed him, gave him a high rank, and treated him as an honored guest rather than a prisoner. This mercy inspired other enemies to surrender peacefully, sparing countless lives.",
    story_ko="후백제의 마지막 왕이 항복했을 때, 왕건은 직접 그를 환영하고, 높은 지위를 주고, 포로가 아닌 귀한 손님으로 대우했습니다. 이 자비는 다른 적들이 평화롭게 항복하도록 영감을 주어, 무수한 생명을 구했습니다.",
    match_message_en="Your features carry the founding wisdom of Wang Geon. There is a merciful, unifying quality to your presence—the look of one who builds lasting kingdoms through wisdom rather than cruelty.",
    match_message_ko="당신의 이목구비는 왕건의 건국 지혜를 담고 있습니다. 당신의 존재에는 자비롭고 통일하는 품질이 있습니다—잔인함보다 지혜로 영속적인 왕국을 건설하는 사람의 모습.",
    image_prompt="Korean founding king in Goryeo royal robes and crown, wise benevolent expression, palace throne room, maps of unified Korea, merciful regal presence",
    visual_description="Wise noble features, merciful knowing eyes, founding king's bearing, expression of diplomatic wisdom and unifying benevolence",
    aliases=["고려 태조", "King Taejo of Goryeo"],
    era="Goryeo Period (877-943 CE)",
    related_characters=["gyeon_hwon", "gung_ye"]
)

GENERAL_GANG_GAM_CHAN_DESC = CharacterDescription(
    id="gang_gam_chan",
    name_en="Gang Gam-chan",
    name_ko="강감찬",
    tagline_en="The Star General, Savior from the Khitan",
    tagline_ko="별의 장군, 거란으로부터의 구원자",
    description_en="""Gang Gam-chan (948-1031 CE) was a scholar-turned-general who saved Goryeo from the massive Khitan Liao invasion of 1018. Legend says he was the reincarnation of a star—when he was born, a great star fell from the sky into his house.

At age 70, when most men would be retired, Gang Gam-chan led 200,000 Goryeo troops against the Khitan army of similar size. At the Battle of Gwiju, he used a dam to trap the Khitan forces, then released the water in a devastating flood attack. Of the Khitan army, only a few thousand survived to flee.

This victory was so complete that the Khitan never invaded Korea again. Gang Gam-chan proved that scholarship and military genius could coexist—he was both a successful civil official and one of Korea's greatest military commanders.""",
    description_ko="""강감찬(948-1031)은 1018년 거대한 거란 요나라의 침략으로부터 고려를 구한 학자 출신 장군입니다. 전설에 따르면 그는 별의 환생이었습니다—그가 태어날 때 큰 별이 하늘에서 그의 집으로 떨어졌다고 합니다.

대부분의 사람들이 은퇴할 70세에, 강감찬은 비슷한 규모의 거란군에 맞서 20만 고려군을 이끌었습니다. 귀주 전투에서 그는 댐을 사용하여 거란군을 가두고, 파괴적인 수공으로 물을 방류했습니다. 거란군 중 단 수천 명만이 도망쳐 살아남았습니다.

이 승리는 너무나 완전하여 거란은 다시는 한국을 침략하지 않았습니다. 강감찬은 학문과 군사적 천재가 공존할 수 있음을 증명했습니다—그는 성공적인 문관이자 한국 최고의 군사 지휘관 중 한 명이었습니다.""",
    traits_en=["Scholarly", "Victorious", "Destined", "Strategic", "Legendary"],
    traits_ko=["학자적인", "승리하는", "운명적인", "전략적인", "전설적인"],
    story_en="When Gang Gam-chan was young and poor, he was so small and thin that people mocked him. But a fortune teller recognized his destiny, saying he was a fallen star destined for greatness. He devoted himself to study, eventually becoming the savior of his nation.",
    story_ko="강감찬이 젊고 가난했을 때, 그는 너무 작고 마른 나머지 사람들이 그를 조롱했습니다. 그러나 한 점쟁이가 그의 운명을 알아보고, 그가 위대함을 위해 운명지어진 떨어진 별이라고 말했습니다. 그는 학문에 전념하여, 결국 나라의 구원자가 되었습니다.",
    match_message_en="Your features carry the destined brilliance of Gang Gam-chan. There is a scholarly yet victorious quality to your presence—the look of one born under a star for greatness.",
    match_message_ko="당신의 이목구비는 강감찬의 운명적인 탁월함을 담고 있습니다. 당신의 존재에는 학자적이면서도 승리하는 품질이 있습니다—위대함을 위해 별 아래 태어난 사람의 모습.",
    image_prompt="Elderly Korean scholar-general in Goryeo armor, thin but commanding, star imagery, dam and flood battle in background, victorious wise expression",
    visual_description="Thin scholarly features transformed by command, star-bright wise eyes, scholar-general bearing, expression of destined victory and intellectual brilliance",
    aliases=["강감찬 장군", "Star General"],
    era="Goryeo Period (948-1031 CE)",
    related_characters=["hyeonjong"]
)

JANG_BOGO_DESC = CharacterDescription(
    id="jang_bogo",
    name_en="Jang Bogo",
    name_ko="장보고",
    tagline_en="King of the Seas, Maritime Emperor",
    tagline_ko="바다의 왕, 해상 황제",
    description_en="""Jang Bogo (died 846 CE) was the greatest maritime figure in Korean history, building a commercial empire that dominated the seas of East Asia. From his base at Cheonghaejin on Wando Island, he controlled the maritime trade routes connecting Korea, China, and Japan.

Rising from common origins, Jang Bogo first made his name as a military commander in Tang China. Returning to Silla, he was outraged to find Korean people being kidnapped and sold as slaves by pirates. He petitioned the king for troops and established Cheonghaejin, creating a naval force that eliminated piracy and protected Korean merchants.

His trading network stretched from the Middle East to Japan. At his peak, no ship could sail the Yellow Sea without his permission. His power grew so great that he became a kingmaker in Silla's court politics—and was eventually assassinated for it.""",
    description_ko="""장보고(사망 846)는 한국 역사상 가장 위대한 해양 인물로, 동아시아의 바다를 지배한 상업 제국을 건설했습니다. 완도 청해진 기지에서 그는 한국, 중국, 일본을 연결하는 해상 무역로를 장악했습니다.

평민 출신에서 일어나, 장보고는 먼저 당나라에서 군사 지휘관으로 이름을 날렸습니다. 신라로 돌아온 그는 해적들에 의해 한국인들이 납치되어 노예로 팔리는 것을 보고 분노했습니다. 그는 왕에게 군대를 청원하여 청해진을 설립하고, 해적을 제거하고 한국 상인들을 보호하는 해군력을 창설했습니다.

그의 무역 네트워크는 중동에서 일본까지 뻗어 있었습니다. 절정기에는 그의 허락 없이는 어떤 배도 황해를 항해할 수 없었습니다. 그의 권력은 신라 궁정 정치에서 왕을 만드는 자가 될 정도로 커졌고—결국 그 때문에 암살되었습니다.""",
    traits_en=["Maritime", "Powerful", "Self-made", "Protective", "Legendary"],
    traits_ko=["해상의", "강력한", "자수성가한", "보호하는", "전설적인"],
    story_en="When Jang Bogo discovered Koreans being sold in Chinese slave markets, he could have simply profited from the trade like others. Instead, he dedicated his life to ending it, creating a naval force strong enough to make the seas safe for his people.",
    story_ko="장보고가 한국인들이 중국 노예 시장에서 팔리는 것을 발견했을 때, 그는 다른 이들처럼 단순히 그 무역에서 이익을 얻을 수 있었습니다. 대신, 그는 그것을 끝내는 데 평생을 바쳐, 자기 민족을 위해 바다를 안전하게 할 만큼 강한 해군력을 창설했습니다.",
    match_message_en="Your features carry the maritime power of Jang Bogo. There is a seafaring, empire-building quality to your presence—the look of one who rules the waves and protects their people.",
    match_message_ko="당신의 이목구비는 장보고의 해상 권력을 담고 있습니다. 당신의 존재에는 항해하고 제국을 건설하는 품질이 있습니다—파도를 다스리고 자기 민족을 보호하는 사람의 모습.",
    image_prompt="Powerful Korean maritime commander on ship deck, commanding the seas, trading ships in background, Cheonghaejin fortress, emperor of the waves presence",
    visual_description="Weathered powerful features, sea-commanding eyes, maritime emperor bearing, expression of protective power and trade empire authority",
    aliases=["장보고 대사", "King of the Yellow Sea"],
    era="Unified Silla Period (died 846 CE)",
    related_characters=["heungdeok_wang"]
)

HWANG_JINI_DESC = CharacterDescription(
    id="hwang_jini",
    name_en="Hwang Jini",
    name_ko="황진이",
    tagline_en="The Legendary Gisaeng, Poet of Desire",
    tagline_ko="전설의 기생, 욕망의 시인",
    description_en="""Hwang Jini (c. 1506-1560) was the most famous gisaeng (courtesan-entertainer) in Korean history and one of its greatest poets. In Joseon society where women had few options, she chose the path of the gisaeng to gain freedom, education, and artistic expression denied to other women.

Her poetry, written in both classical Chinese and the Korean vernacular, expressed passionate emotions with unprecedented frankness. Her sijo (Korean verse) about love, desire, and the passing of time remain among the most beloved works in Korean literature. She was equally famed for her beauty, wit, and skill in music and dance.

Legends tell of her intellectual contests with scholars, Buddhist monks, and noblemen—winning most of them. She is said to have been the only woman who could make the famously stoic scholar Seo Gyeong-deok smile, and the only person who could seduce the devoted Buddhist monk Jijok.""",
    description_ko="""황진이(약 1506-1560)는 한국 역사상 가장 유명한 기생이자 가장 위대한 시인 중 한 명입니다. 여성에게 선택지가 거의 없던 조선 사회에서, 그녀는 다른 여성들에게 거부된 자유, 교육, 예술적 표현을 얻기 위해 기생의 길을 선택했습니다.

한문과 한국어 모두로 쓴 그녀의 시는 전례 없는 솔직함으로 열정적인 감정을 표현했습니다. 사랑, 욕망, 시간의 흐름에 대한 그녀의 시조는 한국 문학에서 가장 사랑받는 작품들 중 하나로 남아 있습니다. 그녀는 아름다움, 재치, 음악과 춤 솜씨로 동등하게 유명했습니다.

전설은 그녀가 학자, 불교 승려, 양반들과 지적 대결을 벌였다고 전합니다—대부분 이겼습니다. 그녀는 유명하게 금욕적인 학자 서경덕을 웃게 할 수 있는 유일한 여성이었고, 헌신적인 불교 승려 지족을 유혹할 수 있는 유일한 사람이었다고 합니다.""",
    traits_en=["Artistic", "Passionate", "Witty", "Free-spirited", "Legendary"],
    traits_ko=["예술적인", "열정적인", "재치 있는", "자유로운 영혼의", "전설적인"],
    story_en="Hwang Jini bet that she could make the monk Jijok break his 30-year vow of celibacy. She waited at a stream he would pass, appearing to struggle. When he carried her across, she clung to him—and he fell. Her victory proved that even the holiest devotion could not resist true beauty and wit.",
    story_ko="황진이는 승려 지족이 30년간의 독신 서약을 어기게 할 수 있다고 내기했습니다. 그녀는 그가 지나갈 개울에서 기다리며, 힘들어하는 척했습니다. 그가 그녀를 건네주려 들어올렸을 때, 그녀가 그에게 매달렸고—그는 넘어졌습니다. 그녀의 승리는 가장 거룩한 헌신도 진정한 아름다움과 재치에 저항할 수 없음을 증명했습니다.",
    match_message_en="Your features carry the captivating artistry of Hwang Jini. There is a passionate, free-spirited quality to your presence—the look of one who lives by beauty, wit, and uncompromising truth.",
    match_message_ko="당신의 이목구비는 황진이의 매혹적인 예술성을 담고 있습니다. 당신의 존재에는 열정적이고 자유로운 영혼의 품질이 있습니다—아름다움, 재치, 타협 없는 진실로 사는 사람의 모습.",
    image_prompt="Beautiful Korean gisaeng in elegant hanbok, holding gayageum or poetry scroll, moonlit pavilion setting, artistic refined beauty, knowing smile",
    visual_description="Stunning refined features, witty knowing eyes, artistic gisaeng bearing, expression of passionate artistry and intellectual freedom",
    aliases=["황진이", "Myeongwol (Bright Moon)"],
    era="Joseon Period (c. 1506-1560)",
    related_characters=["seo_gyeongdeok"]
)

HWARANG_DESC = CharacterDescription(
    id="hwarang",
    name_en="Hwarang (Flower Knights)",
    name_ko="화랑",
    tagline_en="The Flower Knights, Elite Warriors of Silla",
    tagline_ko="화랑, 신라의 정예 전사들",
    description_en="""The Hwarang were an elite corps of young noble warriors in Silla, combining martial training with artistic cultivation, Buddhist philosophy, and absolute loyalty. Their name means "Flower Knights" or "Flowering Youth," reflecting their unique blend of beauty and martial prowess.

Founded in the 6th century, the Hwarang followed the "Five Secular Commandments": loyalty to the king, filial piety, trust among friends, never retreating in battle, and taking life only when necessary. They trained in swordsmanship, archery, and horse riding while also studying poetry, music, and Buddhist scriptures.

Many of Silla's greatest generals, including Kim Yushin, came from the Hwarang. They were instrumental in Silla's unification of the Three Kingdoms. The Hwarang represent the Korean ideal of the warrior-scholar: deadly in battle but refined in peace.""",
    description_ko="""화랑은 신라의 젊은 귀족 전사들로 구성된 정예 부대로, 무술 훈련과 예술적 수양, 불교 철학, 절대적 충성을 결합했습니다. 그들의 이름은 "꽃의 기사" 또는 "꽃피는 청년"을 의미하며, 아름다움과 무예의 독특한 조화를 반영합니다.

6세기에 창설된 화랑은 "세속오계"를 따랐습니다: 왕에 대한 충성, 효도, 친구 간의 신의, 전투에서 물러서지 않음, 필요할 때만 생명을 취함. 그들은 검술, 궁술, 기마술을 훈련하면서도 시, 음악, 불경을 공부했습니다.

김유신을 포함한 신라의 가장 위대한 장군들 많은 이들이 화랑 출신이었습니다. 그들은 신라의 삼국 통일에 핵심적이었습니다. 화랑은 전사-학자의 한국적 이상을 대표합니다: 전투에서는 치명적이지만 평화에서는 세련된.""",
    traits_en=["Elite", "Cultured", "Loyal", "Beautiful", "Deadly"],
    traits_ko=["정예의", "교양 있는", "충성스러운", "아름다운", "치명적인"],
    story_en="Before battle, Hwarang would gather at scenic mountains and rivers to compose poetry, commune with nature, and strengthen their spirits. When combat came, these same youths who had debated philosophy would fight with a ferocity that terrified their enemies.",
    story_ko="전투 전, 화랑은 경치 좋은 산과 강에 모여 시를 짓고, 자연과 교감하고, 정신을 강화했습니다. 전투가 왔을 때, 철학을 토론하던 바로 그 청년들이 적들을 공포에 떨게 하는 맹렬함으로 싸웠습니다.",
    match_message_en="Your features carry the refined deadliness of the Hwarang. There is an elite, cultured quality to your presence—the look of one who masters both sword and poetry.",
    match_message_ko="당신의 이목구비는 화랑의 세련된 치명성을 담고 있습니다. 당신의 존재에는 정예이고 교양 있는 품질이 있습니다—검과 시 모두를 숙달한 사람의 모습.",
    image_prompt="Young Korean noble warriors in elegant Silla attire with weapons, beautiful and deadly, mountain training ground, poetry and swords, elite warrior-poets",
    visual_description="Refined youthful features with warrior's edge, cultured yet fierce eyes, elite warrior-scholar bearing, expression of beauty merged with martial mastery",
    aliases=["화랑도", "Flowering Knights", "Hwarangdo"],
    era="Silla Period (6th-10th century)",
    related_characters=["kim_yushin", "queen_seondeok"]
)

CHOE_YEONG_DESC = CharacterDescription(
    id="choe_yeong",
    name_en="Choe Yeong",
    name_ko="최영",
    tagline_en="The Incorruptible General",
    tagline_ko="청렴결백한 장군",
    description_en="""Choe Yeong (1316-1388) was the most renowned general of late Goryeo, famous equally for his military prowess and his incorruptible character. His father taught him: "Do not be covetous of gold as of a stone." He lived by this principle his entire life.

While other officials amassed fortunes, Choe Yeong remained poor, wearing the same clothes for years and living simply. Yet his military achievements were legendary—he defeated Japanese pirates, suppressed rebellions, and fought against the Red Turban invasions from China.

His downfall came when he opposed his subordinate Yi Seong-gye (future founder of Joseon). When ordered to attack Ming China, Yi Seong-gye instead marched back to the capital in the Wihwado Retreat. The aged Choe Yeong fought to the end but was captured and executed. His integrity made him a symbol of loyalty and incorruptibility.""",
    description_ko="""최영(1316-1388)은 고려 말기의 가장 유명한 장군으로, 무예와 청렴결백한 성품으로 동등하게 유명했습니다. 그의 아버지는 그에게 "황금을 돌 같이 여기라"라고 가르쳤습니다. 그는 평생 이 원칙대로 살았습니다.

다른 관리들이 재산을 모으는 동안, 최영은 가난하게 남아 수년간 같은 옷을 입고 검소하게 살았습니다. 그러나 그의 군사적 업적은 전설적이었습니다—그는 왜구를 물리치고, 반란을 진압하고, 중국에서 온 홍건적 침략과 싸웠습니다.

그의 몰락은 부하 이성계(후의 조선 건국자)에 반대했을 때 왔습니다. 명나라를 공격하라는 명령을 받았을 때, 이성계는 대신 위화도 회군으로 수도로 돌아왔습니다. 노장 최영은 끝까지 싸웠지만 붙잡혀 처형되었습니다. 그의 절개는 그를 충성과 청렴의 상징으로 만들었습니다.""",
    traits_en=["Incorruptible", "Loyal", "Heroic", "Simple", "Principled"],
    traits_ko=["청렴결백한", "충성스러운", "영웅적인", "검소한", "원칙적인"],
    story_en="When Choe Yeong was finally captured after Yi Seong-gye's coup, he refused to bow or show fear. Asked if he had any last wishes, he said only that he hoped Korea would one day defeat the foreign powers threatening it. Even enemies respected his integrity.",
    story_ko="최영이 이성계의 쿠데타 후 마침내 붙잡혔을 때, 그는 굽히거나 두려움을 보이기를 거부했습니다. 마지막 소원이 있냐고 물었을 때, 그는 오직 한국이 언젠가 위협하는 외세를 물리치길 바란다고만 말했습니다. 적들조차 그의 절개를 존경했습니다.",
    match_message_en="Your features carry the incorruptible integrity of Choe Yeong. There is a principled, heroic quality to your presence—the look of one who values honor above gold.",
    match_message_ko="당신의 이목구비는 최영의 청렴결백한 절개를 담고 있습니다. 당신의 존재에는 원칙적이고 영웅적인 품질이 있습니다—금보다 명예를 중히 여기는 사람의 모습.",
    image_prompt="Elderly Korean general in simple armor despite high rank, incorruptible noble bearing, worn but dignified clothes, loyal principled expression",
    visual_description="Weathered noble features showing simple living, principled unwavering eyes, incorruptible warrior bearing, expression of absolute integrity and loyal defiance",
    aliases=["최영 장군", "The Stone General"],
    era="Goryeo Period (1316-1388)",
    related_characters=["yi_seonggye"]
)

YI_BANG_WON_DESC = CharacterDescription(
    id="yi_bang_won",
    name_en="Yi Bang-won (King Taejong)",
    name_ko="이방원 (태종)",
    tagline_en="The Ruthless Builder, Architect of Joseon",
    tagline_ko="냉혹한 건설자, 조선의 설계자",
    description_en="""Yi Bang-won (1367-1422), later King Taejong, was the fifth son of Joseon's founder but became the power behind the throne and eventually the third king. His political genius and ruthlessness shaped Joseon's government for 500 years.

While his father hesitated, Yi Bang-won acted decisively. He personally killed the powerful minister Jeong Do-jeon and eliminated his brothers in the "Strife of Princes" to secure the succession. Once king, he strengthened royal authority, reformed government, and established the systems that made Joseon function.

Most importantly, he recognized that his son Sejong had the wisdom he himself lacked. He ruthlessly removed all obstacles to Sejong's rule, including killing Sejong's father-in-law. His brutality enabled the golden age that followed.""",
    description_ko="""이방원(1367-1422), 후의 태종은 조선 건국자의 다섯째 아들이었지만 왕위 뒤의 권력이 되었고 결국 세 번째 왕이 되었습니다. 그의 정치적 천재성과 냉혹함은 500년간 조선의 정부를 형성했습니다.

그의 아버지가 망설이는 동안, 이방원은 단호하게 행동했습니다. 그는 직접 강력한 대신 정도전을 죽이고 "왕자의 난"에서 형제들을 제거하여 왕위 계승을 확보했습니다. 왕이 된 후, 그는 왕권을 강화하고, 정부를 개혁하고, 조선을 작동하게 하는 시스템을 확립했습니다.

가장 중요하게, 그는 아들 세종이 자신에게 없는 지혜를 가졌음을 인식했습니다. 그는 세종의 장인을 죽이는 것을 포함하여 세종의 통치에 대한 모든 장애물을 냉혹하게 제거했습니다. 그의 잔인함이 뒤따른 황금기를 가능하게 했습니다.""",
    traits_en=["Ruthless", "Brilliant", "Decisive", "Building", "Sacrificing"],
    traits_ko=["냉혹한", "뛰어난", "단호한", "건설하는", "희생하는"],
    story_en="When Yi Bang-won learned that his father-in-law was planning to make Sejong's rival the heir, he immediately ordered the man's execution—despite Sejong's pleas for mercy. He told his son: 'You must hate me for this, but someday you will understand.'",
    story_ko="이방원이 장인이 세종의 라이벌을 후계자로 삼으려 계획하고 있다는 것을 알았을 때, 세종의 자비 호소에도 불구하고 그는 즉시 그 남자의 처형을 명했습니다. 그는 아들에게 말했습니다: '이것 때문에 나를 미워할 것이다, 하지만 언젠가 이해할 것이다.'",
    match_message_en="Your features carry the ruthless brilliance of Taejong. There is a decisive, building quality to your presence—the look of one who does what must be done, whatever the cost.",
    match_message_ko="당신의 이목구비는 태종의 냉혹한 탁월함을 담고 있습니다. 당신의 존재에는 단호하고 건설하는 품질이 있습니다—비용이 무엇이든 해야 할 일을 하는 사람의 모습.",
    image_prompt="Korean king with calculating intense eyes, Joseon royal robes, political mastermind presence, chess-like strategy symbols, powerful decisive bearing",
    visual_description="Sharp calculating features, ruthless but far-seeing eyes, powerful political bearing, expression of decisive ruthlessness and building vision",
    aliases=["태종", "King Taejong of Joseon"],
    era="Joseon Period (1367-1422)",
    related_characters=["sejong", "yi_seonggye", "jeong_dojeon"]
)

SEONBI_DESC = CharacterDescription(
    id="seonbi",
    name_en="Seonbi (Scholar-Gentleman)",
    name_ko="선비",
    tagline_en="The Noble Scholar, Keeper of Principles",
    tagline_ko="고귀한 학자, 원칙의 수호자",
    description_en="""The Seonbi represents the Korean ideal of the virtuous scholar-gentleman—one who pursues knowledge, cultivates moral character, and lives by Confucian principles even at great personal cost. Unlike officials who sought power, the true Seonbi valued integrity above all.

The Seonbi lived simply, often in poverty, studying classical texts and practicing calligraphy in modest homes. They believed that moral cultivation was more important than worldly success. Many famously refused lucrative government positions rather than compromise their principles.

When tyrannical kings demanded obedience, Seonbi scholars often died rather than betray their principles. Their memorial tablets read their crimes as "not bowing to injustice." The Seonbi spirit—valuing righteousness over life, principle over profit—became a defining virtue of Korean identity.""",
    description_ko="""선비는 덕 있는 학자-신사의 한국적 이상을 대표합니다—지식을 추구하고, 도덕적 품성을 함양하며, 큰 개인적 희생에도 유교 원칙대로 사는 사람. 권력을 추구한 관리들과 달리, 진정한 선비는 무엇보다 절개를 중시했습니다.

선비는 검소하게 살았으며, 종종 가난 속에서 검소한 집에서 고전 텍스트를 공부하고 서예를 연습했습니다. 그들은 도덕적 수양이 세속적 성공보다 중요하다고 믿었습니다. 많은 이들이 유명하게 원칙을 타협하기보다 돈벌이가 되는 정부 직위를 거부했습니다.

폭군 왕들이 복종을 요구했을 때, 선비 학자들은 종종 원칙을 배반하기보다 죽었습니다. 그들의 위패에는 죄목으로 "불의에 굽히지 않음"이라 적혀 있었습니다. 선비 정신—생명보다 의로움을, 이익보다 원칙을 중시하는—은 한국 정체성의 결정적 덕목이 되었습니다.""",
    traits_en=["Principled", "Scholarly", "Simple", "Incorruptible", "Noble"],
    traits_ko=["원칙적인", "학자적인", "검소한", "청렴한", "고귀한"],
    story_en="When the tyrant Yeonsangun demanded that scholars praise his unjust policies, many Seonbi refused and were executed. They wrote final poems about bamboo—which bends but never breaks—representing their unbreakable integrity even in death.",
    story_ko="폭군 연산군이 학자들에게 그의 불의한 정책을 칭송하라고 요구했을 때, 많은 선비들이 거부하고 처형되었습니다. 그들은 대나무에 대한 마지막 시를 썼습니다—휘지만 결코 부러지지 않는—죽음에서도 꺾이지 않는 그들의 절개를 대표하는.",
    match_message_en="Your features carry the principled nobility of the Seonbi. There is a scholarly, incorruptible quality to your presence—the look of one who values integrity above all worldly gains.",
    match_message_ko="당신의 이목구비는 선비의 원칙적인 고귀함을 담고 있습니다. 당신의 존재에는 학자적이고 청렴한 품질이 있습니다—모든 세속적 이득보다 절개를 중시하는 사람의 모습.",
    image_prompt="Korean scholar-gentleman in simple white scholar robes, bamboo grove setting, books and calligraphy brushes, modest noble bearing, principled expression",
    visual_description="Refined scholarly features, principled clear eyes, simple noble bearing, expression of uncompromising integrity and cultivated wisdom",
    aliases=["선비정신", "Scholar-Gentleman Spirit"],
    era="Joseon Period (throughout)",
    related_characters=["sejong", "yi_hwang"]
)

AN_JUNG_GEUN_DESC = CharacterDescription(
    id="an_jung_geun",
    name_en="An Jung-geun",
    name_ko="안중근",
    tagline_en="The Patriotic Assassin, Korean Independence Hero",
    tagline_ko="애국적 의사, 한국 독립 영웅",
    description_en="""An Jung-geun (1879-1910) was a Korean independence activist who assassinated Japanese statesman Itō Hirobumi at Harbin Station in 1909. His act of resistance against Japanese colonial aggression made him Korea's most celebrated independence hero.

Before becoming an assassin, An Jung-geun was a Catholic educator and businessman who organized righteous armies against Japanese encroachment. When diplomatic efforts failed and Korea lost its sovereignty, he determined that direct action was necessary.

After his arrest, An Jung-geun conducted himself with such dignity that even his Japanese captors admired him. He wrote extensively about East Asian peace, arguing that Japanese imperialism would ultimately destroy Japan itself. He was executed at 30, becoming a martyr whose sacrifice inspired the Korean independence movement for decades.""",
    description_ko="""안중근(1879-1910)은 1909년 하얼빈역에서 일본 정치가 이토 히로부미를 암살한 한국 독립 운동가입니다. 일본 식민지 침략에 대한 그의 저항 행위는 그를 한국에서 가장 기념받는 독립 영웅으로 만들었습니다.

암살자가 되기 전, 안중근은 일본의 침략에 맞서 의병을 조직한 천주교 교육자이자 사업가였습니다. 외교적 노력이 실패하고 한국이 주권을 잃었을 때, 그는 직접 행동이 필요하다고 결심했습니다.

체포 후, 안중근은 일본인 포획자들조차 그를 존경할 정도로 품위 있게 행동했습니다. 그는 동아시아 평화에 대해 광범위하게 썼으며, 일본 제국주의가 궁극적으로 일본 자체를 파괴할 것이라고 주장했습니다. 그는 30세에 처형되어, 수십 년간 한국 독립 운동에 영감을 준 순교자가 되었습니다.""",
    traits_en=["Patriotic", "Sacrificing", "Principled", "Courageous", "Visionary"],
    traits_ko=["애국적인", "희생하는", "원칙적인", "용감한", "선견지명 있는"],
    story_en="At his trial, An Jung-geun did not beg for mercy but instead listed 15 crimes of Itō Hirobumi against Korea and Asia. His calm, principled defense impressed even the Japanese judges. His final calligraphy read: 'For Korean independence, for East Asian peace.'",
    story_ko="재판에서 안중근은 자비를 구하지 않고 대신 이토 히로부미의 한국과 아시아에 대한 15개 죄목을 열거했습니다. 그의 침착하고 원칙적인 변론은 일본인 재판관들조차 감동시켰습니다. 그의 마지막 서예에는 '대한독립, 동양평화'라고 적혀 있었습니다.",
    match_message_en="Your features carry the patriotic determination of An Jung-geun. There is a sacrificing, principled quality to your presence—the look of one who gives everything for their nation's freedom.",
    match_message_ko="당신의 이목구비는 안중근의 애국적 결의를 담고 있습니다. 당신의 존재에는 희생하고 원칙적인 품질이 있습니다—나라의 자유를 위해 모든 것을 바치는 사람의 모습.",
    image_prompt="Korean independence hero in early 20th century clothing, determined patriotic expression, missing finger (cut for blood oath), Korean flag motif, martyr's dignity",
    visual_description="Intense determined features, patriotic unwavering eyes, martyr's dignified bearing, expression of principled sacrifice and national devotion",
    aliases=["안중근 의사", "Thomas An (Catholic name)"],
    era="Korean Empire/Japanese Colonial Period (1879-1910)",
    related_characters=["ito_hirobumi"]
)


# Dictionary of Korean descriptions (additional to main file)
KOREAN_ADDITIONAL_DESCRIPTIONS = {
    "dangun": DANGUN_DESC,
    "jumong": JUMONG_DESC,
    "gwanggaeto": GWANGGAETO_DESC,
    "eulji_mundeok": EULJI_MUNDEOK_DESC,
    "yeon_gaesomun": YEON_GAESOMUN_DESC,
    "queen_seondeok": QUEEN_SEONDEOK_DESC,
    "kim_yushin": KIM_YUSHIN_DESC,
    "wang_geon": WANG_GEON_DESC,
    "gang_gam_chan": GENERAL_GANG_GAM_CHAN_DESC,
    "jang_bogo": JANG_BOGO_DESC,
    "hwang_jini": HWANG_JINI_DESC,
    "hwarang": HWARANG_DESC,
    "choe_yeong": CHOE_YEONG_DESC,
    "yi_bang_won": YI_BANG_WON_DESC,
    "seonbi": SEONBI_DESC,
    "an_jung_geun": AN_JUNG_GEUN_DESC,
}
