TXT = """
<OPTION value="011-035银行账户">011-035银行账户</OPTION>
<OPTION value="012-001银行账户-中行(RMB)">012-001银行账户-中行(RMB)</OPTION>
<OPTION value="012-035银行账户-瑞穗(RMB)">012-035银行账户-瑞穗(RMB)</OPTION>
<OPTION value="012-036银行账户-瑞穗(USD)">012-036银行账户-瑞穗(USD)</OPTION>
<OPTION value="012-040银行账户-东京三菱(RMB)">012-040银行账户-东京三菱(RMB)</OPTION>
<OPTION value="012-041银行账户-东京三菱(USD)">012-041银行账户-东京三菱(USD)</OPTION>
<OPTION value="012-042银行账户-东京三菱(JPY)">012-042银行账户-东京三菱(JPY)</OPTION>
<OPTION value="012-043银行账户-花旗(RMB)">012-043银行账户-花旗(RMB)</OPTION>
<OPTION value="012-063银行账户-工行(RMB)">012-063银行账户-工行(RMB)</OPTION>
<OPTION value="012-064银行账户-工行陆(RMB)">012-064银行账户-工行陆(RMB)</OPTION>
<OPTION value="012-065银行账户-建行(RMB)">012-065银行账户-建行(RMB)</OPTION>
<OPTION value="012-067银行账户-建行税(RMB)">012-067银行账户-建行税(RMB)</OPTION>
<OPTION value="012-071银行账户-建行(USD)">012-071银行账户-建行(USD)</OPTION>
<OPTION value="012-090银行账户-瑞穗(JPY)">012-090银行账户-瑞穗(JPY)</OPTION>
<OPTION value="012-091银行账户-上行(RMB)">012-091银行账户-上行(RMB)</OPTION>
<OPTION value="025-102运保费">025-102运保费</OPTION>
<OPTION value="025-104关税">025-104关税</OPTION>
<OPTION value="029-001一般消耗材料">029-001一般消耗材料</OPTION>
<OPTION value="029-005计算机消耗材料">029-005计算机消耗材料</OPTION>
<OPTION value="029-006办公用品采购">029-006办公用品采购</OPTION>
<OPTION value="029-012设备备件采购">029-012设备备件采购</OPTION>
<OPTION value="029-013模具关税">029-013模具关税</OPTION>
<OPTION value="029-014仪表采购">029-014仪表采购</OPTION>
<OPTION value="031-080预付保险费">031-080预付保险费</OPTION>
<OPTION value="032-037暂借款">032-037暂借款</OPTION>
<OPTION value="032-506住房保证金">032-506住房保证金</OPTION>
<OPTION value="032-508海关保证金">032-508海关保证金</OPTION>
<OPTION value="032-999其他应收">032-999其他应收</OPTION>
<OPTION value="036-Z03账户划转中转">036-Z03账户划转中转</OPTION>
<OPTION value="038-001进项税-服务业">038-001进项税-服务业</OPTION>
<OPTION value="038-014一般进项税">038-014一般进项税</OPTION>
<OPTION value="038-016进项税-国内旅客运输服务">038-016进项税-国内旅客运输服务</OPTION>
<OPTION value="038-051进项税-海关暂记未抵增值税">038-051进项税-海关暂记未抵增值税</OPTION>
<OPTION value="038-052进项税-进口固定资产">038-052进项税-进口固定资产</OPTION>
<OPTION value="038-053进项税-海关代征">038-053进项税-海关代征</OPTION>
<OPTION value="038-054进项税-运费">038-054进项税-运费</OPTION>
<OPTION value="119-020设备关税">119-020设备关税</OPTION>
<OPTION value="212-008Account Payable-General Purpose">212-008Account Payable-General Purpose</OPTION>
<OPTION value="216-062工伤保险">216-062工伤保险</OPTION>
<OPTION value="216-983基本养老保险">216-983基本养老保险</OPTION>
<OPTION value="216-984基本医疗保险">216-984基本医疗保险</OPTION>
<OPTION value="216-985失业保险">216-985失业保险</OPTION>
<OPTION value="216-986公积金">216-986公积金</OPTION>
<OPTION value="216-990生育保险">216-990生育保险</OPTION>
<OPTION value="216-991奖金">216-991奖金</OPTION>
<OPTION value="232-002代扣营业税">232-002代扣营业税</OPTION>
<OPTION value="241-001个调税">241-001个调税</OPTION>
<OPTION value="241-005印花税">241-005印花税</OPTION>
<OPTION value="241-009代扣所得税">241-009代扣所得税</OPTION>
<OPTION value="241-020代扣河道管理费">241-020代扣河道管理费</OPTION>
<OPTION value="241-021代扣城建税">241-021代扣城建税</OPTION>
<OPTION value="241-022代扣教育费附件">241-022代扣教育费附件</OPTION>
<OPTION value="243-001企业所得税">243-001企业所得税</OPTION>
<OPTION value="244-002Other Payable-Trade">244-002Other Payable-Trade</OPTION>
<OPTION value="244-003代缴养老保险">244-003代缴养老保险</OPTION>
<OPTION value="244-004代缴医疗保险">244-004代缴医疗保险</OPTION>
<OPTION value="244-005代缴失业保险">244-005代缴失业保险</OPTION>
<OPTION value="244-006代缴公积金">244-006代缴公积金</OPTION>
<OPTION value="244-034水电燃气等能源费">244-034水电燃气等能源费</OPTION>
<OPTION value="244-035其他应付款暂记">244-035其他应付款暂记</OPTION>
<OPTION value="244-036日方人员房租">244-036日方人员房租</OPTION>
<OPTION value="244-901关联方非贸易付款">244-901关联方非贸易付款</OPTION>
<OPTION value="245-004终止合同补偿金">245-004终止合同补偿金</OPTION>
<OPTION value="247-001职工工资">247-001职工工资</OPTION>
<OPTION value="247-002外籍员工工资">247-002外籍员工工资</OPTION>
<OPTION value="247-004劳务工费用">247-004劳务工费用</OPTION>
<OPTION value="247-005工会经费">247-005工会经费</OPTION>
<OPTION value="247-902培训费">247-902培训费</OPTION>
<OPTION value="531-373银行手续费">531-373银行手续费</OPTION>
<OPTION value="531-374其他业务-劳务支出">531-374其他业务-劳务支出</OPTION>
<OPTION value="531-909其他业务-材料支出">531-909其他业务-材料支出</OPTION>
<OPTION value="631-016利息收入">631-016利息收入</OPTION>
<OPTION value="702-009工资">702-009工资</OPTION>
<OPTION value="702-102劳务工">702-102劳务工</OPTION>
<OPTION value="706-001人身保险费">706-001人身保险费</OPTION>
<OPTION value="706-031体检费">706-031体检费</OPTION>
<OPTION value="706-064公司旅游">706-064公司旅游</OPTION>
<OPTION value="706-088探亲费等">706-088探亲费等</OPTION>
<OPTION value="706-096工作午餐费">706-096工作午餐费</OPTION>
<OPTION value="706-096餐费">706-096餐费</OPTION>
<OPTION value="706-142医务经费">706-142医务经费</OPTION>
<OPTION value="706-501体检费">706-501体检费</OPTION>
<OPTION value="706-503劳动保护费">706-503劳动保护费</OPTION>
<OPTION value="706-998其他福利费">706-998其他福利费</OPTION>
<OPTION value="711-115成品物流费（货物运输代理服务费，仓储费，力资费，运费）">711-115成品物流费（货物运输代理服务费，仓储费，力资费，运费）</OPTION>
<OPTION value="711-147其他进出口手续费(商检/电脑预录费等)">711-147其他进出口手续费(商检/电脑预录费等)</OPTION>
<OPTION value="711-147商检费">711-147商检费</OPTION>
<OPTION value="711-911运输费">711-911运输费</OPTION>
<OPTION value="712-021办公用品">712-021办公用品</OPTION>
<OPTION value="712-053低值工具">712-053低值工具</OPTION>
<OPTION value="721-028报刊费">721-028报刊费</OPTION>
<OPTION value="722-076人员采用费">722-076人员采用费</OPTION>
<OPTION value="722-083培训费">722-083培训费</OPTION>
<OPTION value="723-047出差机票款国内">723-047出差机票款国内</OPTION>
<OPTION value="723-078车辆使用费（通行费，停车费，洗车费)">723-078车辆使用费（通行费，停车费，洗车费)</OPTION>
<OPTION value="723-079车辆使用费（油费）">723-079车辆使用费（油费）</OPTION>
<OPTION value="723-086班车费">723-086班车费</OPTION>
<OPTION value="724-025出差机票款国外">724-025出差机票款国外</OPTION>
<OPTION value="725-010邮费，快递费">725-010邮费，快递费</OPTION>
<OPTION value="731-111运输保险费">731-111运输保险费</OPTION>
<OPTION value="732-010修理维护费">732-010修理维护费</OPTION>
<OPTION value="732-030除建筑外修理费">732-030除建筑外修理费</OPTION>
<OPTION value="732-035建筑物修理">732-035建筑物修理</OPTION>
<OPTION value="732-991消防费用">732-991消防费用</OPTION>
<OPTION value="736-036保安费">736-036保安费</OPTION>
<OPTION value="736-050排污费 除四害费 废物处理">736-050排污费 除四害费 废物处理</OPTION>
<OPTION value="737-014律师服务">737-014律师服务</OPTION>
<OPTION value="737-021审计费">737-021审计费</OPTION>
<OPTION value="743-011制造费用-仓储费">743-011制造费用-仓储费</OPTION>
<OPTION value="744-006协会会费">744-006协会会费</OPTION>
<OPTION value="744-030文件资料费">744-030文件资料费</OPTION>
<OPTION value="744-393其他办公费(签证费等)">744-393其他办公费(签证费等)</OPTION>
<OPTION value="744-995其他办公费，饮用水，安全标志等">744-995其他办公费，饮用水，安全标志等</OPTION>
<OPTION value="745-063房租">745-063房租</OPTION>
<OPTION value="745-063日方房租">745-063日方房租</OPTION>
<OPTION value="745-110仓储费">745-110仓储费</OPTION>
<OPTION value="745-128车辆租赁费">745-128车辆租赁费</OPTION>
<OPTION value="745-998租赁费其他">745-998租赁费其他</OPTION>
<OPTION value="747-050预计负债 ">747-050预计负债 </OPTION>
<OPTION value="748-015技术支援费">748-015技术支援费</OPTION>
<OPTION value="748-016咨询费">748-016咨询费</OPTION>
<OPTION value="753-002物料消耗">753-002物料消耗</OPTION>
<OPTION value="753-003备品备件">753-003备品备件</OPTION>
<OPTION value="761-005委托外部加工费">761-005委托外部加工费</OPTION>
"""
sep = '>'
pes = '<'
for line in TXT.splitlines():
    if line:
        r = line.split(sep)
        d = r[1].split(pes)
        print(d[0])