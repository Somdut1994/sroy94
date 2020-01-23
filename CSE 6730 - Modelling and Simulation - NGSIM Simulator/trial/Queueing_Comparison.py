delay_e=[21.739636163631122, 0.657596950020793, 0.6318510077150495, 4.368673932984429, 20.425873329961473, 0.6989746365769556, 0.5940372424863712, 4.360602587360545, 24.002571644458843, 0.6252530500209291, 0.4858604042996848, 6.421152089790679, 26.146962557787766, 0.8467133986573547, 0.4754786952564102, 2.8448719873882307, 24.87059028580646, 0.6404859632152778, 0.5655445343312944, 4.020287501146207, 24.321094253037874, 0.7369113947522326, 0.6404657764473234, 5.318029317452754, 18.68854571599982, 0.46838407993334086, 0.38141326498425626, 6.605225776230964, 17.738187343421362, 0.44387392415809335, 0.4333380546249739, 3.6350807327290586, 25.714863238259692, 0.9779504798807038, 0.6337331004876487, 4.430749785507797, 26.158431361414888, 0.8126727742180975, 0.7183663677879214, 4.892136439569234]
runtime_e=[0.00519396737471687, 0.013706555634473266, 0.01943385755615586, 0.024986510191525414, 0.004794322020857219, 0.010043187298275098, 0.015716160207440117, 0.021217897171392674, 0.005116313864678659, 0.010579366296157973, 0.016038720941444984, 0.021758911735834705, 0.005178038449580827, 0.010584201862717135, 0.01592892513604298, 0.021390839787155433, 0.005428065685198366, 0.010971616077633028, 0.016351326097239827, 0.021879516454721887, 0.00484267768644879, 0.010308574568845236, 0.015926080685125826, 0.021473613308844508, 0.005096118263166888, 0.010366885812646831, 0.01603018758869354, 0.023375982082234792, 0.005757737546496111, 0.011885538157313497, 0.018133659041926348, 0.024245815172699414, 0.005548954849177251, 0.01139088814282102, 0.017052198803225727, 0.022458646661453724, 0.005005949169093221, 0.011085678559410755, 0.016479610833603303, 0.021992441156132747]

delay_a=[22.30380953860226, 0.9144230107311391, 0.5511254484755519, 2.938409420747555, 20.564442062318935, 0.6077957743420268, 0.6448470789628451, 4.776888529705122, 20.292948060151097, 0.5304793910140837, 0.5287206097892809, 5.389698530519038, 23.12734606085175, 0.5382641169431425, 0.4986898637513501, 4.704336573321083, 24.62447014059805, 0.568640603481742, 0.5176532982253489, 2.7654437724252694, 24.263155074202558, 0.7422844663911886, 0.6793939867286494, 4.694472193028301, 18.109197969517005, 0.9209952561291872, 0.5461396691526207, 4.3691616015584005, 22.8661550688326, 0.5084995448920882, 0.5891250634118382, 3.7753380253564455, 26.278015688864272, 0.7819361116163965, 0.7343966464868921, 3.169202457132469, 22.069630088972072, 0.7872139667004474, 0.4850875205671938, 2.622984154851065]
runtime_a=[2.016167574567992, 2.8404373969064323, 3.6417513625631006, 4.481733362877697, 1.8871987477589283, 2.69744770263655, 3.466512421574933, 4.227146187994881, 2.5091203051982056, 3.3180397637171506, 4.082385823029073, 4.993307860327219, 2.263885969376073, 2.987717092049559, 3.705830868379577, 4.620216878004628, 2.6815554709173384, 3.4889332370391877, 4.244916895099781, 5.294401807705448, 2.2298444341348898, 3.145979212183807, 3.96762901078246, 5.02173672501868, 2.1526864274464472, 3.2182328166008958, 4.003886942178287, 4.732346555384158, 2.22844467983856, 2.9527704525265435, 3.7166298262865425, 4.726094167823177, 3.025031452516018, 4.018261943778292, 5.0456810283941635, 6.165119806850406, 2.209049222369792, 3.265010949713812, 4.0098136401092646, 4.814758262916584]


runtimes_e=[0, 0, 0, 0]
runtimes_a=[0, 0, 0, 0]

delays_e=[[], [], [], []]
delays_a=[[], [], [], []]
for i in range(10):
	for j in range(4):
		delays_e[j].append(delay_e[i*4+j])
		delays_a[j].append(delay_a[i*4+j])
		runtimes_e[j]+=runtime_e[i*4+j]/10.0
		runtimes_a[j]+=runtime_a[i*4+j]/10.0

servers=['10th St', '11th St', '12th St', '14th St']

def adjustFigAspect(fig,aspect=1):
    '''
    Adjust the subplot parameters so that the figure has the correct
    aspect ratio.
    '''
    xsize,ysize = fig.get_size_inches()
    minsize = min(xsize,ysize)
    xlim = .4*minsize/xsize
    ylim = .4*minsize/ysize
    if aspect < 1:
        xlim *= aspect
    else:
        ylim /= aspect
    fig.subplots_adjust(left=.5-xlim,
                        right=.5+xlim,
                        bottom=.5-ylim,
                        top=.5+ylim)

import matplotlib.pyplot as plt
plt.plot(range(4), runtimes_e, label='Event Oriented')
plt.plot(range(4), runtimes_a, label='Activity Scanning')
plt.xticks(range(4), servers)
plt.yscale('log')
plt.legend()
plt.ylabel('Processor time[s]')
plt.xlabel('Intersection')
plt.title('Execution Time Comparison')
plt.savefig('Runtime_Queueing.png', bbox_inches='tight', dpi=600)
plt.clf()
plt.close()

n=0
for i in servers:
	fig=plt.figure()
	plt.boxplot([delays_e[n], delays_a[n]])
	adjustFigAspect(fig,aspect=.5)
	plt.title('Delay Comparison: '+i)
	plt.xticks((1, 2), ['Event', 'Activity'])
	plt.ylim([0, 1.1*max(max(delays_e[n]), max(delays_a[n]))])
	plt.ylabel('Average Delay[s]')
	plt.xlabel('World View')
	plt.savefig('Delay_'+i+'.png', bbox_inches='tight', dpi=600)
	plt.clf()
	plt.close()
	n+=1
