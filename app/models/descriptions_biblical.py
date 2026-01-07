"""
Biblical Figures - Character Descriptions
Contains descriptions for major figures from the Old and New Testaments
"""
from .descriptions import CharacterDescription


# ============================================
# OLD TESTAMENT FIGURES
# ============================================

MOSES_DESC = CharacterDescription(
    id="moses",
    name_en="Moses",
    name_ko="모세",
    tagline_en="Liberator of Israel, Receiver of the Law",
    tagline_ko="이스라엘의 해방자, 율법의 수여자",
    description_en="""Moses is one of the most significant figures in the Bible, the prophet who led the Israelites out of Egyptian slavery and received the Ten Commandments from God on Mount Sinai. His story spans from being hidden in a basket among the reeds to standing before Pharaoh demanding freedom for his people.

With his brother Aaron at his side, Moses confronted the might of Egypt, calling down the ten plagues that would break Pharaoh's will. He parted the Red Sea, provided water from rocks, and manna from heaven during forty years of wandering in the wilderness.

Moses represents liberation from oppression, the covenant between God and humanity, and the burden of leadership that comes with divine calling.""",
    description_ko="""모세는 성경에서 가장 중요한 인물 중 하나로, 이스라엘 민족을 이집트 노예 생활에서 이끌어내고 시나이 산에서 하나님으로부터 십계명을 받은 예언자입니다. 그의 이야기는 갈대 사이 바구니에 숨겨지는 것에서 시작하여 백성의 자유를 요구하며 파라오 앞에 서는 것까지 이어집니다.

형 아론을 곁에 두고 모세는 이집트의 권력에 맞서 파라오의 의지를 꺾을 열 가지 재앙을 내렸습니다. 그는 홍해를 가르고, 바위에서 물을 내며, 광야에서 40년간 방황하는 동안 하늘에서 만나를 제공했습니다.

모세는 억압으로부터의 해방, 하나님과 인류 사이의 언약, 그리고 신성한 부름과 함께 오는 리더십의 짐을 대표합니다.""",
    traits_en=["Liberating", "Faithful", "Humble", "Persistent", "Lawgiving"],
    traits_ko=["해방하는", "충실한", "겸손한", "끈기 있는", "율법을 주는"],
    story_en="When Moses encountered the burning bush that was not consumed, God called him to free the Israelites. Despite his protests that he was not eloquent, Moses accepted his mission and confronted Pharaoh with the words: 'Let my people go.'",
    story_ko="모세가 타지 않는 불타는 떨기나무를 만났을 때, 하나님은 그에게 이스라엘 민족을 해방하라고 부르셨습니다. 자신이 말을 잘 못한다는 항의에도 불구하고, 모세는 사명을 받아들이고 파라오에게 '내 백성을 보내라'라는 말로 맞섰습니다.",
    match_message_en="Your features carry the determined faith of Moses. There is a liberating presence to your appearance—the look of one called to lead others from bondage to freedom.",
    match_message_ko="당신의 이목구비는 모세의 결연한 믿음을 담고 있습니다. 당신의 외모에는 해방의 존재감이 있습니다—다른 이들을 속박에서 자유로 이끌도록 부름받은 사람의 모습.",
    image_prompt="Bearded prophet in robes holding stone tablets with Ten Commandments, standing on mountain with divine light breaking through clouds, staff in hand, expression of humble authority, biblical epic style",
    visual_description="Weathered wise features, humble yet authoritative gaze, long beard, expression of one who has spoken with the divine",
    aliases=["Moshe", "The Lawgiver"],
    era="Biblical - Old Testament",
    related_characters=["aaron", "miriam", "joshua", "pharaoh"]
)

DAVID_DESC = CharacterDescription(
    id="david",
    name_en="David",
    name_ko="다윗",
    tagline_en="Shepherd King, Psalmist of Israel",
    tagline_ko="목자 왕, 이스라엘의 시편 저자",
    description_en="""David rose from humble shepherd to become Israel's greatest king, a man described as being after God's own heart. His story encompasses both tremendous faith and human failure, from slaying Goliath to his affair with Bathsheba.

As a young shepherd, David's courage and faith led him to face the giant Goliath with only a sling and five stones. As king, he united Israel, captured Jerusalem, and brought the Ark of the Covenant to the city with dancing and celebration.

David represents the complexity of faith—one can be deeply devoted yet deeply flawed, capable of great courage and great sin, always dependent on divine grace for redemption.""",
    description_ko="""다윗은 보잘것없는 목자에서 이스라엘의 가장 위대한 왕이 되었으며, 하나님의 마음에 합한 사람으로 묘사됩니다. 그의 이야기는 골리앗을 죽이는 것에서 밧세바와의 불륜까지, 엄청난 믿음과 인간적 실패를 모두 포함합니다.

어린 목자로서 다윗의 용기와 믿음은 그를 물매와 다섯 개의 돌만으로 거인 골리앗에 맞서게 했습니다. 왕으로서 그는 이스라엘을 통일하고, 예루살렘을 점령했으며, 춤추고 축하하며 언약궤를 도시로 가져왔습니다.

다윗은 믿음의 복잡성을 대표합니다—깊이 헌신하면서도 깊이 결함이 있을 수 있고, 큰 용기와 큰 죄를 저지를 수 있으며, 구원을 위해 항상 신의 은혜에 의존합니다.""",
    traits_en=["Courageous", "Passionate", "Repentant", "Musical", "Complex"],
    traits_ko=["용감한", "열정적인", "회개하는", "음악적인", "복잡한"],
    story_en="When all Israel's warriors feared Goliath, the young shepherd David stepped forward. 'You come against me with sword and spear,' he said, 'but I come against you in the name of the Lord.' A single stone from his sling struck the giant down.",
    story_ko="온 이스라엘 전사들이 골리앗을 두려워할 때, 어린 목자 다윗이 앞으로 나섰습니다. '너는 칼과 창으로 내게 오지만,' 그가 말했습니다, '나는 주의 이름으로 너에게 간다.' 그의 물매에서 나온 하나의 돌이 거인을 쓰러뜨렸습니다.",
    match_message_en="Your features carry the passionate spirit of David. There is a warrior-poet quality to your appearance—the look of one who can fight giants and write psalms, capable of both great courage and deep feeling.",
    match_message_ko="당신의 이목구비는 다윗의 열정적인 영혼을 담고 있습니다. 당신의 외모에는 전사-시인의 품격이 있습니다—거인과 싸우고 시편을 쓸 수 있는, 큰 용기와 깊은 감정 모두를 갖춘 사람의 모습.",
    image_prompt="Young shepherd king with harp and sling, wearing royal robes but with humble bearing, Jerusalem in background, lion at his feet, divine light illuminating his face, biblical heroic style",
    visual_description="Handsome youthful features maturing into kingly wisdom, passionate expressive eyes, appearance of both warrior and poet",
    aliases=["The Sweet Psalmist of Israel", "The Shepherd King"],
    era="Biblical - Old Testament",
    related_characters=["saul", "jonathan", "solomon", "bathsheba", "goliath"]
)

SOLOMON_DESC = CharacterDescription(
    id="solomon",
    name_en="Solomon",
    name_ko="솔로몬",
    tagline_en="Wisest King, Builder of the Temple",
    tagline_ko="가장 지혜로운 왕, 성전 건축자",
    description_en="""Solomon, son of David, is renowned as the wisest person who ever lived. When God offered him anything he desired, Solomon asked only for wisdom to govern his people—and God granted him wisdom beyond any other, along with riches and honor.

His reign was Israel's golden age: he built the magnificent Temple in Jerusalem, authored thousands of proverbs and songs, and his wisdom drew visitors from across the known world, including the Queen of Sheba.

Yet Solomon's story also warns of wisdom's limits—his many foreign wives turned his heart toward their gods, and his kingdom would split after his death. He represents both the heights wisdom can reach and the dangers of straying from it.""",
    description_ko="""다윗의 아들 솔로몬은 역사상 가장 지혜로운 사람으로 유명합니다. 하나님이 그에게 무엇이든 원하는 것을 제안했을 때, 솔로몬은 백성을 다스릴 지혜만을 구했고—하나님은 그에게 다른 누구보다 뛰어난 지혜와 함께 부와 영예를 주셨습니다.

그의 통치는 이스라엘의 황금기였습니다: 그는 예루살렘에 웅장한 성전을 지었고, 수천 개의 잠언과 노래를 저술했으며, 그의 지혜는 스바 여왕을 포함하여 알려진 세계 전역에서 방문객들을 끌어들였습니다.

그러나 솔로몬의 이야기는 지혜의 한계도 경고합니다—그의 많은 이방 아내들이 그의 마음을 그들의 신들에게로 돌렸고, 그의 왕국은 그의 죽음 후에 분열될 것입니다. 그는 지혜가 도달할 수 있는 높이와 그것에서 벗어나는 위험 모두를 대표합니다.""",
    traits_en=["Wise", "Wealthy", "Judicious", "Builder", "Fallen"],
    traits_ko=["지혜로운", "부유한", "판단력 있는", "건축가", "타락한"],
    story_en="Two women claimed the same baby. Solomon ordered the child cut in half—one woman agreed, but the true mother begged for the child to be given to the other woman rather than killed. Solomon immediately gave her the baby, for her love proved her claim.",
    story_ko="두 여인이 같은 아기를 주장했습니다. 솔로몬은 아이를 반으로 자르라고 명령했습니다—한 여인은 동의했지만, 진짜 어머니는 죽이기보다 다른 여인에게 아이를 주라고 간청했습니다. 솔로몬은 즉시 그녀에게 아기를 주었습니다, 그녀의 사랑이 그녀의 주장을 증명했기 때문입니다.",
    match_message_en="Your features carry the discerning wisdom of Solomon. There is a knowing depth to your gaze—the look of one who can see through complexity to find truth at the heart of any matter.",
    match_message_ko="당신의 이목구비는 솔로몬의 분별력 있는 지혜를 담고 있습니다. 당신의 눈빛에는 아는 깊이가 있습니다—복잡함을 꿰뚫어 어떤 문제의 핵심에서 진실을 찾을 수 있는 사람의 모습.",
    image_prompt="Majestic king in golden robes seated on ornate throne, Temple of Jerusalem in background, holding scroll of wisdom, surrounded by treasures and visitors from many lands, divine golden light",
    visual_description="Regal wise features, penetrating intelligent eyes, expression of one who has considered all things under the sun",
    aliases=["Jedidiah", "The Wise King"],
    era="Biblical - Old Testament",
    related_characters=["david", "bathsheba", "queen_of_sheba", "rehoboam"]
)

ABRAHAM_DESC = CharacterDescription(
    id="abraham",
    name_en="Abraham",
    name_ko="아브라함",
    tagline_en="Father of Nations, Friend of God",
    tagline_ko="열국의 아버지, 하나님의 친구",
    description_en="""Abraham is the patriarch of three major world religions—Judaism, Christianity, and Islam. Called by God to leave his homeland and go to a land God would show him, Abraham obeyed, beginning a journey of faith that would shape human history.

God promised Abraham descendants as numerous as the stars, despite his advanced age and his wife Sarah's barrenness. This covenant required Abraham's faith to be tested again and again, culminating in the command to sacrifice his son Isaac.

Abraham represents the foundation of faith—trust in divine promises even when they seem impossible, obedience even when it costs everything, and the blessings that flow from such faithful response.""",
    description_ko="""아브라함은 세 가지 주요 세계 종교—유대교, 기독교, 이슬람교—의 족장입니다. 하나님께서 고향을 떠나 하나님이 보여주실 땅으로 가라고 부르셨을 때, 아브라함은 순종했고, 인류 역사를 형성할 믿음의 여정을 시작했습니다.

하나님은 아브라함에게 그의 고령과 아내 사라의 불임에도 불구하고 별처럼 많은 자손을 약속하셨습니다. 이 언약은 아브라함의 믿음이 반복적으로 시험받아야 했고, 아들 이삭을 제물로 바치라는 명령에서 절정에 달했습니다.

아브라함은 믿음의 기초를 대표합니다—불가능해 보일 때에도 신의 약속을 신뢰하고, 모든 것을 희생해야 할 때에도 순종하며, 그러한 충실한 응답에서 흘러나오는 축복을.""",
    traits_en=["Faithful", "Obedient", "Hospitable", "Tested", "Blessed"],
    traits_ko=["충실한", "순종하는", "환대하는", "시험받는", "축복받은"],
    story_en="God commanded Abraham to sacrifice Isaac, his beloved son of promise. Abraham obeyed, climbing Mount Moriah with wood and knife. Only when Abraham raised the blade did God stop him, providing a ram instead. Abraham's faith was proven complete.",
    story_ko="하나님은 아브라함에게 사랑하는 약속의 아들 이삭을 제물로 바치라고 명령하셨습니다. 아브라함은 순종하여 나무와 칼을 가지고 모리아 산을 올랐습니다. 아브라함이 칼을 들었을 때에야 하나님이 그를 멈추시고 대신 숫양을 제공하셨습니다. 아브라함의 믿음은 완전하다고 증명되었습니다.",
    match_message_en="Your features carry the steadfast faith of Abraham. There is a pilgrim quality to your appearance—the look of one who trusts in promises not yet fulfilled and journeys forward in faith.",
    match_message_ko="당신의 이목구비는 아브라함의 확고한 믿음을 담고 있습니다. 당신의 외모에는 순례자의 품격이 있습니다—아직 이루어지지 않은 약속을 신뢰하고 믿음으로 앞으로 나아가는 사람의 모습.",
    image_prompt="Ancient patriarch with long white beard gazing at star-filled sky, standing in desert with tent behind him, staff in hand, expression of deep faith and wonder, biblical epic atmospheric lighting",
    visual_description="Aged patriarch features, eyes full of faith and wonder, weathered by journey but filled with hope",
    aliases=["Abram", "Father Abraham", "Friend of God"],
    era="Biblical - Old Testament",
    related_characters=["sarah", "isaac", "ishmael", "lot"]
)

ELIJAH_DESC = CharacterDescription(
    id="elijah",
    name_en="Elijah",
    name_ko="엘리야",
    tagline_en="Prophet of Fire, Champion Against Idolatry",
    tagline_ko="불의 선지자, 우상숭배에 맞선 용사",
    description_en="""Elijah was the fiery prophet who confronted the wickedness of King Ahab and Queen Jezebel, standing alone against the prophets of Baal to prove the power of the living God. His ministry was marked by miraculous signs and unwavering courage.

On Mount Carmel, Elijah challenged 450 prophets of Baal to a contest. When their god failed to answer, Elijah called upon the Lord, and fire fell from heaven, consuming the sacrifice and the very stones of the altar.

Elijah represents prophetic boldness—the courage to stand for truth against overwhelming opposition, the power of faith to call down heaven's response, and the reminder that God preserves His faithful servants.""",
    description_ko="""엘리야는 아합 왕과 이세벨 왕비의 악에 맞서 싸운 불 같은 선지자로, 살아계신 하나님의 능력을 증명하기 위해 바알의 선지자들에 홀로 맞섰습니다. 그의 사역은 기적적인 표적과 흔들리지 않는 용기로 특징지어졌습니다.

갈멜 산에서 엘리야는 450명의 바알 선지자들에게 대결을 도전했습니다. 그들의 신이 응답하지 못했을 때, 엘리야는 주님께 부르짖었고, 하늘에서 불이 내려와 제물과 제단의 돌까지 삼켰습니다.

엘리야는 선지자적 담대함을 대표합니다—압도적인 반대에 맞서 진리를 위해 서는 용기, 하늘의 응답을 부르는 믿음의 능력, 그리고 하나님이 충실한 종들을 보존하신다는 것을 상기시켜줍니다.""",
    traits_en=["Bold", "Fiery", "Faithful", "Miraculous", "Zealous"],
    traits_ko=["담대한", "불 같은", "충실한", "기적적인", "열정적인"],
    story_en="On Mount Carmel, after Baal's prophets cried out all day with no answer, Elijah rebuilt the Lord's altar, drenched it with water, and prayed. Fire fell from heaven, consuming everything. The people fell on their faces crying, 'The Lord—He is God!'",
    story_ko="갈멜 산에서, 바알의 선지자들이 하루 종일 부르짖어도 응답이 없은 후, 엘리야는 주님의 제단을 다시 쌓고, 물로 적시고, 기도했습니다. 하늘에서 불이 내려와 모든 것을 삼켰습니다. 백성들은 엎드려 '주 그가 하나님이시다!'라고 외쳤습니다.",
    match_message_en="Your features carry the fiery zeal of Elijah. There is prophetic intensity to your appearance—the look of one who will stand alone for truth if necessary and call upon heaven's power.",
    match_message_ko="당신의 이목구비는 엘리야의 불 같은 열정을 담고 있습니다. 당신의 외모에는 선지자적 강렬함이 있습니다—필요하다면 진리를 위해 홀로 서고 하늘의 능력을 부르는 사람의 모습.",
    image_prompt="Fierce prophet with wild hair and mantle, fire falling from heaven onto altar, dramatic storm clouds, prophets of Baal fleeing, divine flames illuminating his upraised hands, biblical epic style",
    visual_description="Intense weathered features, piercing zealous eyes, wild hair, expression of prophetic fire and unshakeable conviction",
    aliases=["Elias", "The Tishbite"],
    era="Biblical - Old Testament",
    related_characters=["elisha", "ahab", "jezebel", "moses"]
)

SAMSON_DESC = CharacterDescription(
    id="samson",
    name_en="Samson",
    name_ko="삼손",
    tagline_en="Strongman Judge, Nazirite of God",
    tagline_ko="힘센 사사, 하나님의 나실인",
    description_en="""Samson was the strongest man who ever lived, a Nazirite dedicated to God from birth whose legendary strength lay in his uncut hair. He judged Israel for twenty years, single-handedly battling the Philistines who oppressed his people.

His feats were superhuman: he tore a lion apart with bare hands, slew a thousand Philistines with a donkey's jawbone, and carried away the gates of Gaza on his shoulders. Yet his weakness for women, especially Delilah, led to his downfall.

Samson represents the tragedy of squandered gifts—great strength brought low by moral weakness, yet ultimately redeemed in one final act of faith.""",
    description_ko="""삼손은 역사상 가장 힘센 사람이었으며, 태어날 때부터 하나님께 헌신된 나실인으로 그의 전설적인 힘은 자르지 않은 머리카락에 있었습니다. 그는 20년간 이스라엘을 다스리며 백성을 억압하는 블레셋 사람들과 홀로 싸웠습니다.

그의 업적은 초인적이었습니다: 맨손으로 사자를 찢고, 나귀 턱뼈로 천 명의 블레셋 사람을 죽이고, 가자의 성문을 어깨에 메고 갔습니다. 그러나 특히 들릴라를 향한 여인들에 대한 약점이 그의 몰락을 가져왔습니다.

삼손은 낭비된 은사의 비극을 대표합니다—도덕적 약점으로 무너진 큰 힘, 그러나 궁극적으로 마지막 믿음의 행위로 구원받습니다.""",
    traits_en=["Strong", "Nazirite", "Flawed", "Tragic", "Redeemed"],
    traits_ko=["강한", "나실인", "결함 있는", "비극적인", "구원받은"],
    story_en="Blind and chained between the pillars of the Philistine temple, Samson prayed for strength one last time. 'Let me die with the Philistines,' he cried, and pushed against the pillars. The temple collapsed, killing more enemies in his death than in all his life.",
    story_ko="블레셋 성전의 기둥 사이에 눈이 멀고 사슬에 묶인 삼손은 마지막으로 힘을 달라고 기도했습니다. '나로 블레셋 사람들과 함께 죽게 하소서,' 그가 부르짖고 기둥을 밀었습니다. 성전이 무너져 그의 생애보다 죽음에서 더 많은 적을 죽였습니다.",
    match_message_en="Your features carry the raw power of Samson. There is tremendous strength in your appearance—the look of one gifted with extraordinary abilities, called to use them for a purpose greater than self.",
    match_message_ko="당신의 이목구비는 삼손의 순수한 힘을 담고 있습니다. 당신의 외모에는 엄청난 힘이 있습니다—특별한 능력을 부여받고, 자신보다 더 큰 목적을 위해 사용하도록 부름받은 사람의 모습.",
    image_prompt="Massively muscular Hebrew warrior with long flowing hair, breaking chains, Philistines fleeing, temple pillars cracking, dramatic divine light, biblical heroic tragedy style",
    visual_description="Powerfully muscular features, wild long hair, intense eyes showing both strength and inner conflict",
    aliases=["Shimshon", "The Strongman"],
    era="Biblical - Old Testament",
    related_characters=["delilah", "manoah"]
)

ESTHER_DESC = CharacterDescription(
    id="esther",
    name_en="Esther",
    name_ko="에스더",
    tagline_en="Queen of Courage, Savior of Her People",
    tagline_ko="용기의 왕비, 민족을 구한 자",
    description_en="""Esther was a Jewish orphan who became Queen of Persia and saved her people from genocide. Her beauty won the king's heart, but it was her courage that saved a nation when Haman plotted to destroy all Jews in the empire.

Raised by her cousin Mordecai, Esther kept her Jewish identity secret until the moment demanded she reveal it. Knowing she risked death by approaching the king unbidden, she declared, 'If I perish, I perish,' and went to plead for her people.

Esther represents courage in crisis—the willingness to risk everything for others, the power of speaking truth to power, and the providence that places ordinary people in extraordinary positions.""",
    description_ko="""에스더는 페르시아의 왕비가 되어 학살에서 민족을 구한 유대인 고아였습니다. 그녀의 아름다움이 왕의 마음을 사로잡았지만, 하만이 제국의 모든 유대인을 멸망시키려 했을 때 민족을 구한 것은 그녀의 용기였습니다.

사촌 모르드개에게 양육된 에스더는 순간이 요구할 때까지 유대인 정체성을 비밀로 유지했습니다. 초청받지 않고 왕에게 다가가면 죽을 수 있다는 것을 알면서도, 그녀는 '죽으면 죽으리이다'라고 선언하고 민족을 위해 간청하러 갔습니다.

에스더는 위기의 용기를 대표합니다—다른 이들을 위해 모든 것을 걸려는 의지, 권력에게 진실을 말하는 힘, 그리고 평범한 사람들을 비범한 위치에 놓는 섭리를.""",
    traits_en=["Courageous", "Beautiful", "Strategic", "Self-sacrificing", "Faithful"],
    traits_ko=["용감한", "아름다운", "전략적인", "자기희생적인", "충실한"],
    story_en="Esther fasted for three days, then dressed in her royal robes and entered the king's inner court unbidden—a capital offense. When the king extended his golden scepter, she invited him and Haman to a feast where she would reveal Haman's plot and save her people.",
    story_ko="에스더는 사흘간 금식한 후, 왕의 예복을 입고 초청받지 않고 왕의 내전에 들어갔습니다—사형에 해당하는 죄였습니다. 왕이 금홀을 내밀었을 때, 그녀는 왕과 하만을 잔치에 초대하여 하만의 음모를 밝히고 민족을 구했습니다.",
    match_message_en="Your features carry the courageous beauty of Esther. There is regal determination in your appearance—the look of one who would risk everything to protect others and speak truth when silence is easier.",
    match_message_ko="당신의 이목구비는 에스더의 용감한 아름다움을 담고 있습니다. 당신의 외모에는 왕다운 결단력이 있습니다—다른 이들을 보호하기 위해 모든 것을 걸고 침묵이 쉬울 때 진실을 말하는 사람의 모습.",
    image_prompt="Beautiful Persian queen in royal robes and crown, standing before throne room with courage in her eyes, golden light, palace architecture, expression of dignified resolve, biblical drama style",
    visual_description="Beautiful regal features, eyes showing both grace and steel, appearance of dignified courage under pressure",
    aliases=["Hadassah", "The Brave Queen"],
    era="Biblical - Old Testament",
    related_characters=["mordecai", "xerxes", "haman", "vashti"]
)

DANIEL_DESC = CharacterDescription(
    id="daniel",
    name_en="Daniel",
    name_ko="다니엘",
    tagline_en="Prophet in Exile, Interpreter of Dreams",
    tagline_ko="유배 중의 선지자, 꿈의 해석자",
    description_en="""Daniel was a young Hebrew noble taken captive to Babylon who rose to become advisor to kings through his God-given ability to interpret dreams and visions. He served under Nebuchadnezzar, Belshazzar, and Darius while never compromising his faith.

His faithfulness to God brought him into conflict with those who envied his position. When his enemies convinced the king to outlaw prayer, Daniel continued praying openly three times a day, accepting whatever consequence might come.

Daniel represents faithfulness in exile—maintaining integrity in a foreign culture, using gifts to serve while staying true to one's God, and trusting divine deliverance even in the face of death.""",
    description_ko="""다니엘은 바빌론에 포로로 잡혀간 젊은 히브리 귀족으로, 하나님이 주신 꿈과 환상을 해석하는 능력을 통해 왕들의 고문이 되었습니다. 그는 느부갓네살, 벨사살, 다리오 밑에서 섬기면서도 결코 믿음을 타협하지 않았습니다.

하나님께 대한 충실함은 그의 위치를 시기하는 자들과 갈등을 가져왔습니다. 그의 적들이 왕에게 기도를 불법화하도록 설득했을 때, 다니엘은 어떤 결과가 오든 받아들이며 하루 세 번 공개적으로 기도를 계속했습니다.

다니엘은 유배 중의 충실함을 대표합니다—이방 문화에서 정직을 유지하고, 자신의 하나님께 충실하면서 은사를 사용하여 섬기며, 죽음 앞에서도 신의 구원을 신뢰하는 것을.""",
    traits_en=["Faithful", "Wise", "Visionary", "Uncompromising", "Prophetic"],
    traits_ko=["충실한", "현명한", "예언적 비전이 있는", "타협하지 않는", "선지자적인"],
    story_en="Daniel's enemies had him thrown into the lions' den for praying to God. King Darius spent a sleepless night, then rushed to the den at dawn. Daniel called out, 'My God sent his angel and shut the lions' mouths.' He emerged without a scratch.",
    story_ko="다니엘의 적들은 하나님께 기도했다는 이유로 그를 사자 굴에 던지게 했습니다. 다리오 왕은 밤새 잠을 이루지 못하고, 새벽에 굴로 달려갔습니다. 다니엘이 외쳤습니다, '내 하나님이 천사를 보내사 사자들의 입을 막으셨나이다.' 그는 상처 하나 없이 나왔습니다.",
    match_message_en="Your features carry the unwavering faith of Daniel. There is visionary wisdom in your gaze—the look of one who sees beyond the present moment and remains faithful despite every pressure.",
    match_message_ko="당신의 이목구비는 다니엘의 흔들리지 않는 믿음을 담고 있습니다. 당신의 눈빛에는 예언적 지혜가 있습니다—현재 순간을 넘어 보고 모든 압력에도 충실한 사람의 모습.",
    image_prompt="Noble Hebrew prophet in Babylonian court robes, lions at his feet miraculously tamed, divine light protecting him, prophetic visions swirling in background, expression of peaceful faith, biblical epic style",
    visual_description="Noble dignified features, clear prophetic eyes, calm faithful expression, appearance of one at peace with God regardless of circumstances",
    aliases=["Belteshazzar", "The Prophet"],
    era="Biblical - Old Testament",
    related_characters=["nebuchadnezzar", "shadrach", "meshach", "abednego"]
)

RUTH_DESC = CharacterDescription(
    id="ruth",
    name_en="Ruth",
    name_ko="룻",
    tagline_en="Faithful Daughter, Ancestor of Kings",
    tagline_ko="충실한 며느리, 왕들의 조상",
    description_en="""Ruth was a Moabite woman who, after her Hebrew husband died, chose to leave her homeland and follow her mother-in-law Naomi back to Israel. Her famous declaration of loyalty—'Where you go I will go'—is one of the Bible's most beautiful expressions of devotion.

Though a foreigner with nothing, Ruth's faithful hard work in the fields of Boaz caught his attention. Her story became one of redemption and blessing—she married Boaz and became the great-grandmother of King David.

Ruth represents faithful love across all boundaries—the choice to stay loyal when leaving would be easier, the reward of humble diligence, and God's grace that includes outsiders in the covenant story.""",
    description_ko="""룻은 히브리인 남편이 죽은 후 고향을 떠나 시어머니 나오미를 따라 이스라엘로 돌아가기로 선택한 모압 여인이었습니다. 그녀의 유명한 충성 선언—'어머니가 가시는 곳에 나도 가겠나이다'—은 성경에서 가장 아름다운 헌신의 표현 중 하나입니다.

아무것도 없는 외국인이었지만, 보아스의 밭에서 충실히 일하는 룻의 모습은 그의 관심을 끌었습니다. 그녀의 이야기는 구원과 축복 중 하나가 되었습니다—그녀는 보아스와 결혼하여 다윗 왕의 증조할머니가 되었습니다.

룻은 모든 경계를 넘는 충실한 사랑을 대표합니다—떠나는 것이 더 쉬울 때 충성하기로 선택하는 것, 겸손한 근면의 보상, 그리고 이방인을 언약의 이야기에 포함시키는 하나님의 은혜를.""",
    traits_en=["Faithful", "Humble", "Loyal", "Hardworking", "Blessed"],
    traits_ko=["충실한", "겸손한", "충성스러운", "근면한", "축복받은"],
    story_en="Naomi told Ruth to return to Moab, but Ruth refused: 'Where you go I will go, and where you stay I will stay. Your people will be my people and your God my God.' Her loyalty led her to Israel, to Boaz, and into the lineage of the Messiah.",
    story_ko="나오미가 룻에게 모압으로 돌아가라고 했지만, 룻은 거부했습니다: '어머니가 가시는 곳에 나도 가고, 머무시는 곳에 나도 머물겠나이다. 어머니의 백성이 내 백성이 되고 어머니의 하나님이 내 하나님이 되시리이다.' 그녀의 충성은 그녀를 이스라엘로, 보아스에게로, 그리고 메시아의 혈통으로 이끌었습니다.",
    match_message_en="Your features carry the faithful devotion of Ruth. There is loyal steadfastness in your appearance—the look of one who stays true through hardship and finds blessing in faithfulness.",
    match_message_ko="당신의 이목구비는 룻의 충실한 헌신을 담고 있습니다. 당신의 외모에는 충성스러운 꾸준함이 있습니다—어려움 속에서도 진실하게 남고 충실함에서 축복을 찾는 사람의 모습.",
    image_prompt="Young Moabite woman gleaning wheat in golden fields, humble but dignified bearing, Bethlehem in background, soft warm light, expression of faithful determination and humble hope, biblical pastoral style",
    visual_description="Humble beautiful features, loyal steadfast eyes, appearance of faithful devotion and quiet strength",
    aliases=["The Moabite", "Great-grandmother of David"],
    era="Biblical - Old Testament",
    related_characters=["naomi", "boaz", "david", "obed"]
)


# ============================================
# NEW TESTAMENT FIGURES
# ============================================

MARY_MOTHER_DESC = CharacterDescription(
    id="mary_mother",
    name_en="Mary, Mother of Jesus",
    name_ko="성모 마리아",
    tagline_en="Blessed Mother, Handmaid of the Lord",
    tagline_ko="복되신 어머니, 주의 종",
    description_en="""Mary is the virgin mother of Jesus Christ, chosen by God to bear the Savior of the world. Her humble acceptance of the angel Gabriel's announcement—'I am the Lord's servant'—set in motion the central event of Christian faith.

From the joyous birth in Bethlehem to standing at the foot of the cross, Mary's journey encompassed the highest joy and deepest sorrow. She pondered all things in her heart, faithfully supporting her son's ministry even when she could not fully understand it.

Mary represents perfect faith and surrender to God's will—the courage to say yes to the impossible, the strength to endure unspeakable loss, and the blessed role of bringing Christ into the world.""",
    description_ko="""마리아는 예수 그리스도의 동정녀 어머니로, 세상의 구세주를 낳도록 하나님께 선택되었습니다. 천사 가브리엘의 선포에 대한 그녀의 겸손한 수락—'나는 주의 종이오니'—이 기독교 신앙의 중심 사건을 시작했습니다.

베들레헴에서의 기쁜 탄생부터 십자가 아래 서 있기까지, 마리아의 여정은 가장 큰 기쁨과 가장 깊은 슬픔을 포함했습니다. 그녀는 모든 것을 마음에 간직하며, 완전히 이해할 수 없을 때에도 아들의 사역을 충실히 지지했습니다.

마리아는 완전한 믿음과 하나님의 뜻에 대한 항복을 대표합니다—불가능에 예라고 말하는 용기, 형언할 수 없는 상실을 견디는 힘, 그리고 그리스도를 세상에 가져오는 축복된 역할을.""",
    traits_en=["Faithful", "Humble", "Blessed", "Sorrowful", "Pondering"],
    traits_ko=["충실한", "겸손한", "축복받은", "슬픔 가득한", "묵상하는"],
    story_en="When the angel told Mary she would bear God's Son, she asked only how this could be since she was a virgin. Assured it would be through the Holy Spirit, Mary responded: 'I am the Lord's servant. May it be to me according to your word.'",
    story_ko="천사가 마리아에게 하나님의 아들을 낳을 것이라고 말했을 때, 그녀는 처녀이므로 어떻게 이 일이 될 수 있는지만 물었습니다. 성령으로 될 것이라는 확신을 받은 마리아는 대답했습니다: '나는 주의 종이오니 말씀대로 내게 이루어지이다.'",
    match_message_en="Your features carry the blessed grace of Mary. There is pure devotion in your appearance—the look of one who accepts God's will with humble faith and treasures sacred things in the heart.",
    match_message_ko="당신의 이목구비는 마리아의 축복받은 은혜를 담고 있습니다. 당신의 외모에는 순수한 헌신이 있습니다—겸손한 믿음으로 하나님의 뜻을 받아들이고 거룩한 것들을 마음에 간직하는 사람의 모습.",
    image_prompt="Beautiful young woman in blue veil, humble yet radiating grace, divine light illuminating her gentle face, holding infant or with hands in prayer, expression of serene acceptance and deep faith, Renaissance sacred art style",
    visual_description="Serene gentle features, eyes full of faith and wonder, appearance of humble grace and divine blessing",
    aliases=["The Virgin Mary", "Our Lady", "Madonna"],
    era="Biblical - New Testament",
    related_characters=["jesus", "joseph", "elizabeth", "john"]
)

PETER_DESC = CharacterDescription(
    id="peter",
    name_en="Peter",
    name_ko="베드로",
    tagline_en="Rock of the Church, Chief of Apostles",
    tagline_ko="교회의 반석, 사도들의 수장",
    description_en="""Peter was a simple fisherman whom Jesus called to become the leader of his apostles. Impetuous and passionate, Peter often spoke before thinking—yet his confession 'You are the Christ' became the rock upon which the church was built.

Peter's story is one of failure and restoration. He promised to die for Jesus, then denied knowing him three times. But after the resurrection, Jesus restored Peter with the command to 'Feed my sheep,' and Peter became the fearless leader of the early church.

Peter represents the transforming power of grace—that our failures need not define us, that Christ can build his church on imperfect people, and that love covers a multitude of sins.""",
    description_ko="""베드로는 예수님께서 사도들의 지도자가 되라고 부르신 평범한 어부였습니다. 충동적이고 열정적인 베드로는 종종 생각하기 전에 말했지만—그의 고백 '주는 그리스도시니이다'는 교회가 세워진 반석이 되었습니다.

베드로의 이야기는 실패와 회복의 이야기입니다. 그는 예수님을 위해 죽겠다고 약속했지만, 세 번이나 그를 모른다고 부인했습니다. 그러나 부활 후 예수님은 '내 양을 먹이라'는 명령으로 베드로를 회복시켰고, 베드로는 초대 교회의 두려움 없는 지도자가 되었습니다.

베드로는 은혜의 변화시키는 능력을 대표합니다—우리의 실패가 우리를 정의할 필요가 없다는 것, 그리스도께서 불완전한 사람들 위에 교회를 세울 수 있다는 것, 그리고 사랑이 많은 죄를 덮는다는 것을.""",
    traits_en=["Impetuous", "Faithful", "Restored", "Bold", "Leading"],
    traits_ko=["충동적인", "충실한", "회복된", "담대한", "이끄는"],
    story_en="After Jesus' arrest, Peter denied knowing him three times before the rooster crowed, just as Jesus predicted. After the resurrection, Jesus asked Peter three times, 'Do you love me?' and three times commanded, 'Feed my sheep'—restoring him completely.",
    story_ko="예수님이 잡히신 후, 베드로는 예수님이 예언하신 대로 닭이 울기 전에 세 번 그를 모른다고 부인했습니다. 부활 후, 예수님은 베드로에게 세 번 '네가 나를 사랑하느냐?' 물으시고 세 번 '내 양을 먹이라' 명하셨습니다—그를 완전히 회복시켜 주셨습니다.",
    match_message_en="Your features carry the bold faith of Peter. There is passionate strength in your appearance—the look of one who fails and rises again, who leads through imperfection by grace.",
    match_message_ko="당신의 이목구비는 베드로의 담대한 믿음을 담고 있습니다. 당신의 외모에는 열정적인 힘이 있습니다—실패하고 다시 일어서며, 은혜로 불완전함 속에서 이끄는 사람의 모습.",
    image_prompt="Weathered fisherman turned apostle, holding keys of the kingdom, expression of passionate faith and humble restoration, Jerusalem or fishing boat in background, biblical drama style",
    visual_description="Weathered rugged features, passionate earnest eyes, appearance of one transformed from simple fisherman to bold leader",
    aliases=["Simon Peter", "Cephas", "The Rock"],
    era="Biblical - New Testament",
    related_characters=["jesus", "andrew", "james", "john"]
)

PAUL_DESC = CharacterDescription(
    id="paul",
    name_en="Paul",
    name_ko="바울",
    tagline_en="Apostle to the Gentiles, Writer of Epistles",
    tagline_ko="이방인의 사도, 서신서 저자",
    description_en="""Paul was Christianity's greatest missionary, transformed from Saul the persecutor to Paul the apostle by an encounter with the risen Christ on the road to Damascus. He traveled thousands of miles establishing churches and wrote much of the New Testament.

His letters to churches in Rome, Corinth, Galatia, and elsewhere form the theological foundation of Christian faith. He suffered shipwrecks, beatings, imprisonment, and eventually martyrdom—yet counted it all as nothing compared to knowing Christ.

Paul represents radical transformation—that the greatest enemies can become the greatest advocates, that God's grace is sufficient for any weakness, and that nothing can separate us from the love of Christ.""",
    description_ko="""바울은 기독교 역사상 가장 위대한 선교사로, 다마스쿠스로 가는 길에서 부활하신 그리스도와의 만남을 통해 박해자 사울에서 사도 바울로 변화되었습니다. 그는 수천 마일을 여행하며 교회들을 세웠고 신약성경의 많은 부분을 저술했습니다.

로마, 고린도, 갈라디아 등의 교회들에 보낸 그의 서신들은 기독교 신앙의 신학적 기초를 형성합니다. 그는 난파, 구타, 투옥, 그리고 결국 순교를 겪었지만—그리스도를 아는 것에 비하면 모든 것을 아무것도 아닌 것으로 여겼습니다.

바울은 급진적인 변화를 대표합니다—가장 큰 적이 가장 큰 옹호자가 될 수 있다는 것, 하나님의 은혜가 어떤 약점에도 충분하다는 것, 그리고 아무것도 우리를 그리스도의 사랑에서 끊을 수 없다는 것을.""",
    traits_en=["Transformed", "Zealous", "Intellectual", "Suffering", "Tireless"],
    traits_ko=["변화된", "열정적인", "지적인", "고통받는", "지칠 줄 모르는"],
    story_en="Saul was breathing murderous threats against Christians when a blinding light struck him down. 'Saul, why do you persecute me?' Jesus asked. Three days blind, Saul was transformed. He emerged as Paul, who would carry the gospel to the ends of the earth.",
    story_ko="사울이 그리스도인들에 대해 살기 등등하게 위협하고 있을 때 눈부신 빛이 그를 쓰러뜨렸습니다. '사울아, 네가 어찌하여 나를 박해하느냐?' 예수님이 물으셨습니다. 사흘간 눈이 먼 후, 사울은 변화되었습니다. 그는 복음을 땅 끝까지 전할 바울로 다시 태어났습니다.",
    match_message_en="Your features carry the zealous transformation of Paul. There is intellectual fire in your appearance—the look of one changed completely by encounter with truth, tireless in sharing it with others.",
    match_message_ko="당신의 이목구비는 바울의 열정적인 변화를 담고 있습니다. 당신의 외모에는 지적인 불꽃이 있습니다—진리와의 만남으로 완전히 변화되어, 다른 이들과 나누기를 지치지 않는 사람의 모습.",
    image_prompt="Intense apostle in Roman prison writing epistles, scroll and quill in hand, chains on wrists, divine light illuminating theological vision in eyes, expression of passionate conviction, biblical dramatic style",
    visual_description="Intense intellectual features, fiery passionate eyes, appearance of one consumed by divine mission",
    aliases=["Saul of Tarsus", "The Apostle"],
    era="Biblical - New Testament",
    related_characters=["jesus", "peter", "barnabas", "timothy", "luke"]
)

JOHN_APOSTLE_DESC = CharacterDescription(
    id="john_apostle",
    name_en="John the Apostle",
    name_ko="사도 요한",
    tagline_en="The Beloved Disciple, Author of Love",
    tagline_ko="사랑받는 제자, 사랑의 저자",
    description_en="""John was the apostle closest to Jesus, traditionally identified as 'the disciple whom Jesus loved.' He was present at the Transfiguration, leaned on Jesus' chest at the Last Supper, and stood at the foot of the cross when Jesus entrusted Mary to his care.

The only apostle believed to have died of natural causes in old age, John wrote the Gospel of John, three epistles, and the Book of Revelation. His writings emphasize love as the central command and the mystical union of believers with Christ.

John represents intimate relationship with Christ—the beloved disciple who emphasizes that 'God is love' and calls all believers to love one another as proof of knowing God.""",
    description_ko="""요한은 예수님께 가장 가까운 사도로, 전통적으로 '예수께서 사랑하시는 제자'로 알려져 있습니다. 그는 변화산에 함께 있었고, 최후의 만찬에서 예수님의 품에 기대었으며, 예수님이 마리아를 그에게 맡기실 때 십자가 아래 서 있었습니다.

노년에 자연사한 것으로 믿어지는 유일한 사도인 요한은 요한복음, 세 서신, 그리고 요한계시록을 저술했습니다. 그의 글은 사랑을 중심 계명으로 강조하고 신자들과 그리스도의 신비로운 연합을 강조합니다.

요한은 그리스도와의 친밀한 관계를 대표합니다—'하나님은 사랑이시라'를 강조하고 모든 신자들에게 하나님을 안다는 증거로 서로 사랑하라고 부르는 사랑받는 제자.""",
    traits_en=["Beloved", "Loving", "Visionary", "Mystical", "Faithful"],
    traits_ko=["사랑받는", "사랑하는", "예언적 비전이 있는", "신비로운", "충실한"],
    story_en="At the Last Supper, John leaned against Jesus to ask who would betray him. At the cross, Jesus looked at John and Mary and said, 'Woman, behold your son' and 'Behold your mother.' From that hour, John took Mary into his home.",
    story_ko="최후의 만찬에서 요한은 누가 배반할 것인지 물으려고 예수님께 기대었습니다. 십자가에서 예수님은 요한과 마리아를 보시고 '여자여, 보라 네 아들이니라' 그리고 '보라 네 어머니라' 말씀하셨습니다. 그 시간부터 요한은 마리아를 자기 집으로 모셨습니다.",
    match_message_en="Your features carry the loving spirit of John. There is deep devotion in your appearance—the look of one who understands that love is the heart of all truth and all relationship with the divine.",
    match_message_ko="당신의 이목구비는 요한의 사랑하는 영혼을 담고 있습니다. 당신의 외모에는 깊은 헌신이 있습니다—사랑이 모든 진리의 핵심이며 신성과의 모든 관계의 핵심임을 이해하는 사람의 모습.",
    image_prompt="Elderly apostle with gentle expression writing on scroll, eagle symbol nearby, divine visions of Revelation in background, expression of deep love and mystical understanding, warm golden light",
    visual_description="Gentle aged features, eyes full of deep love and understanding, appearance of one who has known intimate divine relationship",
    aliases=["John the Evangelist", "The Beloved Disciple"],
    era="Biblical - New Testament",
    related_characters=["jesus", "peter", "james", "mary_mother"]
)

MARY_MAGDALENE_DESC = CharacterDescription(
    id="mary_magdalene",
    name_en="Mary Magdalene",
    name_ko="막달라 마리아",
    tagline_en="Witness to the Resurrection, Apostle to the Apostles",
    tagline_ko="부활의 증인, 사도들에게 보내진 사도",
    description_en="""Mary Magdalene was a devoted follower of Jesus from whom he cast out seven demons. She traveled with Jesus and the disciples, supported his ministry, and remained faithful when others fled—standing at the cross and being first at the empty tomb.

On Easter morning, Mary was the first person to see the risen Christ, who commissioned her to tell the disciples. Her message—'I have seen the Lord!'—makes her the first evangelist of the resurrection, earning her the title 'Apostle to the Apostles.'

Mary represents redemption and devoted witness—the transformed life that stays faithful through darkness and is honored with being first to proclaim the central truth of Christian faith.""",
    description_ko="""막달라 마리아는 예수님께서 일곱 귀신을 쫓아내신 헌신적인 추종자였습니다. 그녀는 예수님과 제자들과 함께 여행하고, 그의 사역을 지원했으며, 다른 이들이 도망쳤을 때도 충실하게 남아—십자가 아래 서 있었고 빈 무덤에 가장 먼저 있었습니다.

부활절 아침, 마리아는 부활하신 그리스도를 처음 본 사람이었고, 그리스도께서는 그녀에게 제자들에게 전하라고 명하셨습니다. 그녀의 메시지—'내가 주를 보았노라!'—는 그녀를 부활의 첫 전도자로 만들어, '사도들에게 보내진 사도'라는 칭호를 얻게 했습니다.

마리아는 구원과 헌신적인 증인을 대표합니다—어둠 속에서도 충실하게 남아 기독교 신앙의 중심 진리를 처음 선포하는 영예를 받은 변화된 삶을.""",
    traits_en=["Devoted", "Redeemed", "Faithful", "Witnessing", "Honored"],
    traits_ko=["헌신적인", "구원받은", "충실한", "증거하는", "영예로운"],
    story_en="Mary came to the tomb while it was still dark and found it empty. Weeping, she saw a man she thought was the gardener. 'Mary,' Jesus said. She recognized him instantly and cried 'Rabboni!'—then ran to tell the disciples: 'I have seen the Lord!'",
    story_ko="마리아가 아직 어두울 때 무덤에 왔고 비어 있는 것을 발견했습니다. 울면서 그녀는 동산지기라고 생각한 사람을 보았습니다. '마리아야,' 예수님이 말씀하셨습니다. 그녀는 즉시 그를 알아보고 '랍오니!'라고 외쳤습니다—그리고 달려가 제자들에게 말했습니다: '내가 주를 보았노라!'",
    match_message_en="Your features carry the devoted faithfulness of Mary Magdalene. There is redeemed joy in your appearance—the look of one transformed by grace and faithful to witness truth in every circumstance.",
    match_message_ko="당신의 이목구비는 막달라 마리아의 헌신적인 충실함을 담고 있습니다. 당신의 외모에는 구원받은 기쁨이 있습니다—은혜로 변화되어 모든 상황에서 진리를 증거하는 충실한 사람의 모습.",
    image_prompt="Devoted woman at empty tomb at dawn, expression of joyful recognition and wonder, first light of resurrection morning, tears transformed to joy, running to share good news, biblical sacred moment style",
    visual_description="Expressive emotional features, eyes showing both tears and joy, appearance of profound devotion and transforming encounter",
    aliases=["Mary of Magdala", "Apostle to the Apostles"],
    era="Biblical - New Testament",
    related_characters=["jesus", "mary_mother", "peter", "john_apostle"]
)


NOAH_DESC = CharacterDescription(
    id="noah",
    name_en="Noah",
    name_ko="노아",
    tagline_en="Builder of the Ark, Survivor of the Flood",
    tagline_ko="방주의 건축자, 홍수의 생존자",
    description_en="""Noah was the righteous man chosen by God to survive the great flood that would cleanse the world of its wickedness. For decades, he faithfully built an enormous ark according to God's precise instructions, enduring the mockery of his neighbors.

When the rains came, Noah, his family, and pairs of every living creature found refuge in the ark. For forty days and nights the deluge fell, and for months the waters covered the earth before finally receding.

Noah represents faithful obedience in the face of ridicule, the preservation of life through divine instruction, and the covenant relationship symbolized by the rainbow.""",
    description_ko="""노아는 세상의 악을 씻어낼 대홍수에서 살아남도록 하나님께 선택된 의로운 사람이었습니다. 수십 년간 그는 하나님의 정확한 지시에 따라 거대한 방주를 충실히 지었고, 이웃들의 조롱을 견뎠습니다.

비가 왔을 때, 노아와 그의 가족, 그리고 모든 생물의 쌍이 방주에서 피난처를 찾았습니다. 40일 밤낮으로 폭우가 내렸고, 물이 마침내 빠지기 전 몇 달 동안 땅을 덮었습니다.

노아는 조롱 앞에서의 충실한 순종, 신성한 지시를 통한 생명의 보존, 그리고 무지개로 상징되는 언약 관계를 대표합니다.""",
    traits_en=["Righteous", "Obedient", "Patient", "Preserving", "Faithful"],
    traits_ko=["의로운", "순종하는", "인내하는", "보존하는", "충실한"],
    story_en="After the flood, Noah released a dove that returned with an olive branch—proof that dry land had appeared. When the family finally left the ark, God set a rainbow in the sky as a sign of His promise never to destroy the earth by flood again.",
    story_ko="홍수 후, 노아는 비둘기를 놓아주었고 올리브 가지를 물고 돌아왔습니다—마른 땅이 나타났다는 증거였습니다. 가족이 마침내 방주를 떠났을 때, 하나님은 다시는 홍수로 땅을 멸망시키지 않겠다는 약속의 표시로 하늘에 무지개를 두셨습니다.",
    match_message_en="Your features carry the patient righteousness of Noah. There is steadfast determination in your appearance—the look of one who will faithfully complete their calling regardless of what others think.",
    match_message_ko="당신의 이목구비는 노아의 인내하는 의로움을 담고 있습니다. 당신의 외모에는 꾸준한 결단력이 있습니다—다른 사람들이 어떻게 생각하든 충실하게 부름을 완수할 사람의 모습.",
    image_prompt="Ancient patriarch overseeing construction of massive wooden ark, animals gathering in background, stormy sky approaching, expression of determined faith, biblical epic scale",
    visual_description="Weathered patriarch features, determined faithful eyes, appearance of one who endures despite opposition",
    aliases=["The Preacher of Righteousness"],
    era="Biblical - Old Testament",
    related_characters=["shem", "ham", "japheth"]
)

JOB_DESC = CharacterDescription(
    id="job",
    name_en="Job",
    name_ko="욥",
    tagline_en="The Suffering Servant, Faith Through Affliction",
    tagline_ko="고난받는 종, 고통 속의 믿음",
    description_en="""Job was a blameless and upright man who lost everything—his children, his wealth, his health—yet refused to curse God. His story explores the deepest questions of why the righteous suffer and how faith endures through undeserved pain.

When even his wife told him to curse God and die, and his friends insisted his suffering must be punishment for sin, Job maintained his integrity. He questioned, he raged, he demanded answers from God—but he never abandoned his faith.

Job represents the mystery of suffering, the inadequacy of easy answers, and the ultimate restoration that comes from encountering God directly rather than merely knowing about Him.""",
    description_ko="""욥은 흠 없고 정직한 사람으로 모든 것—자녀들, 재산, 건강—을 잃었지만 하나님을 저주하기를 거부했습니다. 그의 이야기는 왜 의로운 자가 고통받는지, 받을 자격 없는 고통 속에서 어떻게 믿음이 견디는지에 대한 가장 깊은 질문을 탐구합니다.

아내조차 그에게 하나님을 저주하고 죽으라고 했고, 친구들은 그의 고통이 죄에 대한 벌이라고 주장했지만, 욥은 자신의 정직함을 유지했습니다. 그는 질문했고, 분노했고, 하나님께 답을 요구했습니다—그러나 결코 믿음을 버리지 않았습니다.

욥은 고통의 신비, 쉬운 답의 부적절함, 그리고 하나님에 대해 단순히 아는 것보다 직접 만남으로써 오는 궁극적인 회복을 대표합니다.""",
    traits_en=["Suffering", "Faithful", "Questioning", "Honest", "Restored"],
    traits_ko=["고통받는", "충실한", "질문하는", "정직한", "회복된"],
    story_en="After losing everything, Job sat in ashes scraping his boils. His friends argued that he must have sinned, but Job maintained his innocence. Finally, God spoke from a whirlwind, and Job said, 'I had heard of you, but now my eyes have seen you.' God restored him double.",
    story_ko="모든 것을 잃은 후, 욥은 재 가운데 앉아 종기를 긁었습니다. 친구들은 그가 틀림없이 죄를 지었다고 주장했지만, 욥은 자신의 무죄를 주장했습니다. 마침내 하나님이 회오리바람에서 말씀하셨고, 욥은 말했습니다, '내가 주에 대하여 귀로 듣기만 하였사오나 이제는 눈으로 주를 뵈옵나이다.' 하나님은 그에게 배로 회복시켜 주셨습니다.",
    match_message_en="Your features carry the tested faith of Job. There is enduring strength in your appearance—the look of one who has faced the deepest questions and emerged with faith intact.",
    match_message_ko="당신의 이목구비는 욥의 시험받은 믿음을 담고 있습니다. 당신의 외모에는 견디는 힘이 있습니다—가장 깊은 질문들에 직면하고 믿음을 온전히 유지한 채 나온 사람의 모습.",
    image_prompt="Afflicted man sitting in ashes, covered in sores but eyes lifted to heaven, divine light breaking through storm clouds, friends in background, expression of questioning faith, biblical dramatic style",
    visual_description="Suffering weathered features, eyes showing pain yet unbroken faith, appearance of one who questions yet still believes",
    aliases=["The Patient One"],
    era="Biblical - Old Testament",
    related_characters=["eliphaz", "bildad", "zophar", "elihu"]
)

JACOB_DESC = CharacterDescription(
    id="jacob",
    name_en="Jacob",
    name_ko="야곱",
    tagline_en="Patriarch of Israel, Wrestler with God",
    tagline_ko="이스라엘의 족장, 하나님과 씨름한 자",
    description_en="""Jacob was the grandson of Abraham who deceived his father to steal his brother Esau's blessing, yet became the father of the twelve tribes of Israel. His name means 'supplanter' or 'deceiver,' but after wrestling with God, he was renamed Israel—'one who struggles with God.'

His life was marked by both trickery and transformation. He tricked Esau and was tricked by Laban. He fled his homeland and eventually returned to face his brother, but on that night, he wrestled with a mysterious figure until dawn and refused to let go without a blessing.

Jacob represents the human struggle with both God and self—the deceiver who becomes a patriarch, the wrestler who limps away blessed, the transformation that comes from encounter with the divine.""",
    description_ko="""야곱은 아버지를 속여 형 에서의 축복을 훔친 아브라함의 손자였지만, 이스라엘의 열두 지파의 아버지가 되었습니다. 그의 이름은 '대신하는 자' 또는 '속이는 자'를 의미하지만, 하나님과 씨름한 후 이스라엘—'하나님과 겨루는 자'로 개명되었습니다.

그의 삶은 속임수와 변화 모두로 특징지어졌습니다. 그는 에서를 속였고 라반에게 속았습니다. 그는 고향을 떠났다가 결국 형을 만나러 돌아왔지만, 그 밤에 신비로운 인물과 새벽까지 씨름하며 축복을 받지 않고는 놓아주지 않았습니다.

야곱은 하나님과 자신 모두와의 인간적 투쟁을 대표합니다—족장이 된 속이는 자, 축복받아 절뚝거리며 떠나는 씨름꾼, 신과의 만남에서 오는 변화를.""",
    traits_en=["Struggling", "Transformed", "Persistent", "Blessed", "Fathering"],
    traits_ko=["투쟁하는", "변화된", "끈기 있는", "축복받은", "아버지가 되는"],
    story_en="The night before meeting Esau, Jacob wrestled with a mysterious man until dawn. When the man saw he could not prevail, he touched Jacob's hip, dislocating it. Still Jacob held on: 'I will not let you go unless you bless me.' He was renamed Israel and walked away limping but blessed.",
    story_ko="에서를 만나기 전날 밤, 야곱은 새벽까지 신비한 사람과 씨름했습니다. 그 사람이 이길 수 없음을 보고 야곱의 엉덩이를 쳐서 탈구시켰습니다. 그래도 야곱은 붙잡았습니다: '당신이 나를 축복하지 않으면 보내지 않겠나이다.' 그는 이스라엘로 개명되었고 절뚝거리지만 축복받아 떠났습니다.",
    match_message_en="Your features carry the wrestling spirit of Jacob. There is persistent determination in your appearance—the look of one who struggles but refuses to let go until they receive their blessing.",
    match_message_ko="당신의 이목구비는 야곱의 씨름하는 정신을 담고 있습니다. 당신의 외모에는 끈기 있는 결단력이 있습니다—투쟁하지만 축복을 받을 때까지 놓아주지 않는 사람의 모습.",
    image_prompt="Patriarch wrestling with divine figure at night by river Jabbok, dawn breaking, expression of determined struggle and transformation, divine light, biblical dramatic encounter",
    visual_description="Strong determined features, eyes showing both cunning and transformation, appearance of one who has wrestled and been changed",
    aliases=["Israel", "The Supplanter"],
    era="Biblical - Old Testament",
    related_characters=["abraham", "isaac", "esau", "rachel", "leah"]
)

ISAIAH_DESC = CharacterDescription(
    id="isaiah",
    name_en="Isaiah",
    name_ko="이사야",
    tagline_en="Prince of Prophets, Voice of Hope",
    tagline_ko="선지자들의 왕자, 소망의 목소리",
    description_en="""Isaiah is considered the greatest of the Hebrew prophets, serving during the reigns of four kings and delivering some of the most beautiful and challenging prophecies in Scripture. His vision of God in the temple transformed him from a man of unclean lips to God's willing messenger.

His prophecies span judgment and hope, warning of exile yet promising restoration. His messianic prophecies—of a virgin bearing a son, a suffering servant, a prince of peace—have been central to Jewish and Christian understanding of God's salvation plan.

Isaiah represents prophetic vision that sees beyond the immediate to God's ultimate purposes, the call to speak difficult truths, and the hope that shines even in the darkest predictions of judgment.""",
    description_ko="""이사야는 히브리 선지자들 중 가장 위대한 것으로 여겨지며, 네 왕의 통치 기간 동안 섬기고 성경에서 가장 아름답고 도전적인 예언을 전했습니다. 성전에서 하나님을 본 그의 환상은 그를 더러운 입술의 사람에서 하나님의 기꺼이 하는 메신저로 변화시켰습니다.

그의 예언은 심판과 소망을 아우르며, 유배를 경고하면서도 회복을 약속합니다. 처녀가 아들을 낳고, 고난받는 종, 평화의 왕자에 대한 그의 메시아 예언은 하나님의 구원 계획에 대한 유대인과 기독교인의 이해에 중심이 되어 왔습니다.

이사야는 즉각적인 것을 넘어 하나님의 궁극적인 목적을 보는 선지자적 비전, 어려운 진실을 말하라는 부름, 그리고 심판의 가장 어두운 예언 속에서도 빛나는 소망을 대표합니다.""",
    traits_en=["Visionary", "Eloquent", "Bold", "Hopeful", "Prophetic"],
    traits_ko=["비전이 있는", "웅변적인", "담대한", "희망적인", "선지자적인"],
    story_en="Isaiah saw the Lord high and exalted in the temple, with seraphim calling 'Holy, holy, holy.' Overwhelmed by his unworthiness, Isaiah cried out. A seraph touched his lips with a burning coal: 'Your guilt is taken away.' When God asked, 'Whom shall I send?' Isaiah answered, 'Here am I. Send me!'",
    story_ko="이사야는 주님이 성전에서 높이 들려 영광스러우신 것을 보았고, 스랍들이 '거룩하다, 거룩하다, 거룩하다'고 외치고 있었습니다. 자신의 부족함에 압도되어 이사야가 외쳤습니다. 스랍 하나가 불붙는 숯으로 그의 입술을 만졌습니다: '네 죄가 사라졌느니라.' 하나님이 '내가 누구를 보내며?' 물으셨을 때 이사야가 대답했습니다, '제가 여기 있나이다. 나를 보내소서!'",
    match_message_en="Your features carry the visionary eloquence of Isaiah. There is prophetic depth in your gaze—the look of one who sees beyond the present moment to speak words of both challenge and hope.",
    match_message_ko="당신의 이목구비는 이사야의 비전 있는 웅변력을 담고 있습니다. 당신의 눈빛에는 선지자적 깊이가 있습니다—현재 순간을 넘어 보고 도전과 희망의 말씀을 하는 사람의 모습.",
    image_prompt="Majestic prophet in temple with seraphim flying above, divine glory filling space, lips touched by burning coal, expression of transformed calling, biblical visionary scene",
    visual_description="Noble prophetic features, eyes that have seen divine glory, expression of one commissioned to speak truth",
    aliases=["The Prince of Prophets"],
    era="Biblical - Old Testament",
    related_characters=["hezekiah", "micah", "jeremiah"]
)

JOHN_BAPTIST_DESC = CharacterDescription(
    id="john_baptist",
    name_en="John the Baptist",
    name_ko="세례 요한",
    tagline_en="Voice in the Wilderness, Forerunner of the Messiah",
    tagline_ko="광야의 소리, 메시아의 선구자",
    description_en="""John the Baptist was the prophet sent to prepare the way for Jesus Christ. Living in the wilderness, clothed in camel's hair and eating locusts and honey, he called all Israel to repentance and baptized them in the Jordan River.

When Jesus came to be baptized, John recognized him as the Lamb of God who takes away the sin of the world. Though he was the greatest prophet, John declared himself unworthy to untie Jesus' sandals and said, 'He must increase, but I must decrease.'

John represents the prophetic voice that prepares hearts for God's coming, the humility that points away from self toward the greater One, and the courage that speaks truth to power regardless of consequences.""",
    description_ko="""세례 요한은 예수 그리스도를 위해 길을 예비하도록 보내진 선지자였습니다. 광야에서 살며, 낙타 털옷을 입고 메뚜기와 야생 꿀을 먹으며, 그는 온 이스라엘에게 회개를 촉구하고 요단강에서 세례를 주었습니다.

예수님이 세례를 받으러 오셨을 때, 요한은 그를 세상 죄를 지고 가는 하나님의 어린 양으로 알아보았습니다. 그가 가장 위대한 선지자였지만, 요한은 자신이 예수님의 신발끈을 풀기에도 부족하다고 선언하며 '그는 흥하여야 하겠고 나는 쇠하여야 하리라'고 말했습니다.

요한은 하나님의 오심을 위해 마음을 준비하는 선지자적 목소리, 자신을 떠나 더 큰 분을 가리키는 겸손, 그리고 결과에 상관없이 권력에게 진실을 말하는 용기를 대표합니다.""",
    traits_en=["Preparing", "Humble", "Bold", "Wilderness", "Decreasing"],
    traits_ko=["준비하는", "겸손한", "담대한", "광야의", "쇠하는"],
    story_en="When Herodias wanted John dead for condemning her marriage to Herod, her daughter Salome danced for the king and asked for John's head. Herod, though he feared John, granted her request. John died faithful to his calling to speak truth.",
    story_ko="헤로디아가 헤롯과의 결혼을 정죄한 요한을 죽이기를 원했을 때, 그녀의 딸 살로메가 왕을 위해 춤을 추고 요한의 머리를 요구했습니다. 헤롯은 요한을 두려워했지만 그녀의 요청을 들어주었습니다. 요한은 진실을 말하라는 부름에 충실하게 죽었습니다.",
    match_message_en="Your features carry the wilderness strength of John the Baptist. There is prophetic boldness in your appearance—the look of one who prepares the way and points others to truth greater than themselves.",
    match_message_ko="당신의 이목구비는 세례 요한의 광야의 힘을 담고 있습니다. 당신의 외모에는 선지자적 담대함이 있습니다—길을 준비하고 다른 이들에게 자신보다 더 큰 진리를 가리키는 사람의 모습.",
    image_prompt="Wild prophet in camel hair at Jordan River, baptizing crowds, wilderness behind him, pointing to heaven, rugged but holy appearance, divine light, biblical prophetic style",
    visual_description="Rugged wilderness features, intense prophetic eyes, wild appearance but holy bearing, expression of one pointing beyond himself",
    aliases=["The Baptist", "The Forerunner"],
    era="Biblical - New Testament",
    related_characters=["jesus", "herod", "salome", "elizabeth", "zechariah"]
)

JONAH_DESC = CharacterDescription(
    id="jonah",
    name_en="Jonah",
    name_ko="요나",
    tagline_en="The Reluctant Prophet, Messenger to Nineveh",
    tagline_ko="마지못해 하는 선지자, 니느웨로의 메신저",
    description_en="""Jonah is the prophet who ran from God's call to preach to Nineveh, Israel's enemy. He boarded a ship going the opposite direction, but God sent a great storm. When the sailors cast Jonah overboard, a great fish swallowed him whole.

After three days in the belly of the fish, Jonah prayed and was vomited onto dry land. He finally preached to Nineveh, and to his frustration, the entire city repented and was spared.

Jonah represents the human tendency to resist God's wider purposes, the impossibility of escaping divine calling, and God's mercy that extends even to our enemies—a mercy we often struggle to share.""",
    description_ko="""요나는 이스라엘의 적인 니느웨에 전파하라는 하나님의 부름에서 도망친 선지자입니다. 그는 반대 방향으로 가는 배에 탔지만, 하나님은 큰 폭풍을 보내셨습니다. 선원들이 요나를 바다에 던졌을 때, 큰 물고기가 그를 통째로 삼켰습니다.

물고기 뱃속에서 사흘 후, 요나는 기도했고 마른 땅에 토해졌습니다. 그는 마침내 니느웨에 전파했고, 그의 좌절감에, 온 도시가 회개하여 살아남았습니다.

요나는 하나님의 더 넓은 목적에 저항하는 인간의 경향, 신성한 부름에서 벗어나는 것의 불가능함, 그리고 우리의 적들에게까지 미치는 하나님의 자비—우리가 종종 나누기 힘들어하는 자비를 대표합니다.""",
    traits_en=["Reluctant", "Running", "Swallowed", "Preaching", "Angry"],
    traits_ko=["마지못해 하는", "도망치는", "삼켜진", "전파하는", "화난"],
    story_en="Inside the great fish, Jonah prayed: 'From the depths of Sheol I called for help, and you listened to my cry.' After three days, the fish vomited Jonah onto dry land. This time, when God said 'Go to Nineveh,' Jonah went.",
    story_ko="큰 물고기 안에서 요나는 기도했습니다: '스올 깊은 곳에서 내가 도움을 청했더니 주께서 내 음성을 들으셨나이다.' 사흘 후 물고기가 요나를 마른 땅에 토해냈습니다. 이번에 하나님이 '니느웨로 가라' 하셨을 때, 요나는 갔습니다.",
    match_message_en="Your features carry the reluctant journey of Jonah. There is honest struggle in your appearance—the look of one learning that God's purposes are wider than our preferences and His mercy more generous than our own.",
    match_message_ko="당신의 이목구비는 요나의 마지못해 하는 여정을 담고 있습니다. 당신의 외모에는 정직한 투쟁이 있습니다—하나님의 목적이 우리의 선호보다 넓고 그분의 자비가 우리 자신의 것보다 더 관대하다는 것을 배우고 있는 사람의 모습.",
    image_prompt="Prophet being spit out by great fish onto shore, expression of reluctant surrender, Nineveh visible in distance, dramatic ocean scene, biblical dramatic style",
    visual_description="Reluctant determined features, eyes showing inner conflict between duty and desire, appearance of one who runs but cannot escape calling",
    aliases=["The Reluctant Prophet"],
    era="Biblical - Old Testament",
    related_characters=["ninevites"]
)


# Dictionary of Biblical descriptions
BIBLICAL_DESCRIPTIONS = {
    # Old Testament
    "moses": MOSES_DESC,
    "david": DAVID_DESC,
    "solomon": SOLOMON_DESC,
    "abraham": ABRAHAM_DESC,
    "elijah": ELIJAH_DESC,
    "samson": SAMSON_DESC,
    "esther": ESTHER_DESC,
    "daniel": DANIEL_DESC,
    "ruth": RUTH_DESC,
    "noah": NOAH_DESC,
    "job": JOB_DESC,
    "jacob": JACOB_DESC,
    "isaiah": ISAIAH_DESC,
    "jonah": JONAH_DESC,
    # New Testament
    "mary_mother": MARY_MOTHER_DESC,
    "peter": PETER_DESC,
    "paul": PAUL_DESC,
    "john_apostle": JOHN_APOSTLE_DESC,
    "john_baptist": JOHN_BAPTIST_DESC,
    "mary_magdalene": MARY_MAGDALENE_DESC,
}
