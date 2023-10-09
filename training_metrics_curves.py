import numpy as np
import matplotlib.pyplot as plt



y = np.arange(1, 21, 1)

fig, axs = plt.subplots(2, 3)


# Dataset
with open(r'C:\Users\gaoyi\Documents\MA_data\training_metrics\record_metrics_original.txt') as f:
    RMSE = []
    rel = []
    log10 = []
    delata1 = []
    delata2 = []
    delata3 = []

    lines = f.readlines()
    print(lines)
    x = [line.split(',') for line in lines]
    print(x[0])
    for i in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]:
        RMSE.append(float(x[i][0]))
        rel.append(float(x[i][2]))
        log10.append(float(x[i][3]))
        delata1.append(float(x[i][4]))
        delata2.append(float(x[i][5]))
        delata3.append(float(x[i][6]))


    # Plotting the Graph



    # plt.plot(y, RMSE)
    # plt.plot(y, rel)
    # plt.plot(y, log10)
    # plt.plot(y, delata1)
    # plt.plot(y, delata2)
    # plt.plot(y, delata3)

    # plt.xlim([0, 20])
    # plt.ylim([0, 1])
    #
    #
    # plt.title("Evaluation metrics")
    # plt.xlabel("Epoch")
    # plt.ylabel("RMSE")
    # plt.show()


    ######################


    # axs[0, 0].bar(x + 0.00, PESQ[0], color = 'b', width = 0.1, label='PESQ_Input')
    # axs[0, 0].bar(x , PESQ[1], color = 'r', width = 0.1, label='PESQ_Speech')
    axs[0, 0].plot(y, RMSE, 'b', label='original')
    # axs[0, 0].plot(x, PESQ[2], 'gs-', label='PESQ_CPU')
    #
    #
    axs[0, 0].legend(loc="upper right", prop={'size': 6})
    # axs[0, 0].set_xticklabels(['tf241','tf251'])
    # axs[0, 0].set_xticks(x)
    axs[0, 0].set_ylabel("RMSE")
    # axs[0, 0].set_ylim([1.97, 2.05])
    #
    # print(STOI[1])
    #
    #
    # ######################
    #
    # STOI_CPU=[0.871064045980629, 0.86959292595979]
    #
    # ######################
    #
    # STOI = [STOI_Input, STOI_Speech, STOI_CPU]
    #
    #
    # # axs[0, 1].bar(x + 0.00, STOI[0], color = 'b', width = 0.1, label='STOI_Input')
    # # axs[0, 1].bar(x , STOI[1], color = 'r', width = 0.1, label='STOI_Speech')
    axs[0, 1].plot(y, rel, 'b', label='original')
    # axs[0, 1].plot(x, STOI[2], 'gs-', label='STOI_CPU')
    #
    #
    #
    #
    axs[0, 1].legend(loc="upper right", prop={'size': 6})
    # axs[0, 1].set_xticklabels(['tf241','tf251'])
    # axs[0, 1].set_xticks(x)
    axs[0, 1].set_ylabel("rel")
    # axs[0, 1].set_ylim([0.865, 0.875])
    #
    # print(ESTOI[1])
    #
    #
    # ######################
    # ESTOI_CPU=[0.706688077027074, 0.703560301040584]
    # ######################
    # ESTOI = [ESTOI_Input, ESTOI_Speech, ESTOI_CPU]
    #
    # # axs[0, 2].bar(x + 0.00, ESTOI[0], color = 'b', width = 0.1, label='ESTOI_Input')
    # # axs[0, 2].bar(x , ESTOI[1], color = 'r', width = 0.1, label='ESTOI_Speech')
    axs[0, 2].plot(y, log10, 'b', label='original')
    # axs[0, 2].plot(x, ESTOI[2], 'gs-', label='ESTOI_CPU')
    #
    #
    axs[0, 2].legend(loc="upper right", prop={'size': 7})
    # axs[0, 2].set_xticklabels(['tf241','tf251'])
    # axs[0, 2].set_xticks(x)
    axs[0, 2].set_ylabel("log10")
    # axs[0, 2].set_ylim([0.69, 0.73])
    #
    # print(SDR[1])
    #
    # ######################
    # SDR_CPU=[12.7247550577017, 12.7428309180384]
    # ######################
    # SDR = [SDR_Input, SDR_Speech, SDR_CPU]
    #
    #
    #
    #
    # # axs[1, 0].bar(x + 0.00, SDR[0], color = 'b', width = 0.1, label='SDR_Input')
    # # axs[1, 0].bar(x , SDR[1], color = 'r', width = 0.1, label='SDR_Speech')
    axs[1, 0].plot(y, delata1, 'b', label='original')
    # axs[1, 0].plot(x, SDR[2], 'gs-', label='SDR_CPU')
    #
    #
    #
    #
    #
    axs[1, 0].legend(loc="lower right", prop={'size': 6})
    # axs[1, 0].set_xticklabels(['tf241','tf251'])
    # axs[1, 0].set_xticks(x)
    axs[1, 0].set_ylabel("Delata1")
    # axs[1, 0].set_ylim([12.65, 12.85])
    #
    # print(SIR[1])
    # ######################
    # SIR_CPU=[18.0760909892901, 18.1720442495923]
    # ######################
    # SIR = [SIR_Input, SIR_Speech, SIR_CPU]
    #
    # # axs[1, 1].bar(x + 0.00, SIR[0], color = 'b', width = 0.1, label='SIR_Input')
    # # axs[1, 1].bar(x , SIR[1], color = 'r', width = 0.1, label='SIR_Speech')
    axs[1, 1].plot(y, delata2, 'b', label='original')
    # axs[1, 1].plot(x, SIR[2], 'gs-', label='SIR_CPU')
    #
    #
    #
    axs[1, 1].legend(loc="lower right", prop={'size': 6})
    # axs[1, 1].set_xticklabels(['tf241','tf251'])
    # axs[1, 1].set_xticks(x)
    axs[1, 1].set_ylabel("Delata2")
    # axs[1, 1].set_ylim([17.91, 18.5])
    #
    # print(SAR[1])
    #
    # ######################
    # SAR_CPU=[14.3904900734593, 14.3699187556171]
    # ######################
    # SAR = [SAR_Input, SAR_Speech, SAR_CPU]
    #
    # # axs[1, 2].bar(x + 0.00, SAR[0], color = 'b', width = 0.1, label='SAR_Input')
    # # axs[1, 2].bar(x, SAR[1], color = 'r', width = 0.1, label='SAR_Speech')
    axs[1, 2].plot(y, delata3, 'b', label='original')
    # axs[1, 2].plot(x, SAR[2], 'gs-', label='SAR_CPU')
    #

    axs[1, 2].legend(loc="lower right", prop={'size': 6})
    # axs[1, 2].set_xticklabels(['tf221', 'tf231', 'tf241'])
    # axs[1, 2].set_xticks(x)
    axs[1, 2].set_ylabel("Delata3")
    # axs[1, 2].set_ylim([14.15, 14.6])
    #

with open(r'C:\Users\gaoyi\Documents\MA_data\training_metrics\record_metrics_after_up2.txt') as f:
    RMSE = []
    rel = []
    log10 = []
    delata1 = []
    delata2 = []
    delata3 = []

    lines = f.readlines()
    print(lines)
    x = [line.split(',') for line in lines]
    print(x[0])
    for i in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]:
        RMSE.append(float(x[i][0]))
        rel.append(float(x[i][2]))
        log10.append(float(x[i][3]))
        delata1.append(float(x[i][4]))
        delata2.append(float(x[i][5]))
        delata3.append(float(x[i][6]))


    ######################


    axs[0, 0].plot(y, RMSE, 'g', label='ordinalentropy1')
    axs[0, 0].legend(loc="upper right", prop={'size': 6})
    axs[0, 0].set_ylabel("RMSE")

    axs[0, 1].plot(y, rel, 'g', label='ordinalentropy1')
    axs[0, 1].legend(loc="upper right", prop={'size': 6})
    axs[0, 1].set_ylabel("rel")

    axs[0, 2].plot(y, log10, 'g', label='ordinalentropy1')
    axs[0, 2].legend(loc="upper right", prop={'size': 7})
    axs[0, 2].set_ylabel("log10")

    axs[1, 0].plot(y, delata1, 'g', label='ordinalentropy1')
    axs[1, 0].legend(loc="lower right", prop={'size': 6})
    axs[1, 0].set_ylabel("Delata1")


    axs[1, 1].plot(y, delata2, 'g', label='ordinalentropy1')
    axs[1, 1].legend(loc="lower right", prop={'size': 6})
    axs[1, 1].set_ylabel("Delata2")


    axs[1, 2].plot(y, delata3, 'g', label='ordinalentropy1')
    axs[1, 2].legend(loc="lower right", prop={'size': 6})
    axs[1, 2].set_ylabel("Delata3")


with open(r'C:\Users\gaoyi\Documents\MA_data\training_metrics\record_metrics_before_up3_2.txt') as f:
    RMSE = []
    rel = []
    log10 = []
    delata1 = []
    delata2 = []
    delata3 = []

    lines = f.readlines()
    print(lines)
    x = [line.split(',') for line in lines]
    print(x[0])
    for i in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]:
        RMSE.append(float(x[i][0]))
        rel.append(float(x[i][2]))
        log10.append(float(x[i][3]))
        delata1.append(float(x[i][4]))
        delata2.append(float(x[i][5]))
        delata3.append(float(x[i][6]))

    ######################


    axs[0, 0].plot(y, RMSE, 'r', label='ordinalentropy2')
    axs[0, 0].legend(loc="upper right", prop={'size': 6})
    axs[0, 0].set_ylabel("RMSE")



    axs[0, 1].plot(y, rel, 'r', label='ordinalentropy2')
    axs[0, 1].legend(loc="upper right", prop={'size': 6})
    axs[0, 1].set_ylabel("rel")


    axs[0, 2].plot(y, log10, 'r', label='ordinalentropy2')
    axs[0, 2].legend(loc="upper right", prop={'size': 7})
    axs[0, 2].set_ylabel("log10")



    axs[1, 0].plot(y, delata1, 'r', label='ordinalentropy2')
    axs[1, 0].legend(loc="lower right", prop={'size': 6})
    axs[1, 0].set_ylabel("Delata1")



    axs[1, 1].plot(y, delata2, 'r', label='ordinalentropy2')
    axs[1, 1].legend(loc="lower right", prop={'size': 6})
    axs[1, 1].set_ylabel("Delata2")



    axs[1, 2].plot(y, delata3, 'r', label='ordinalentropy2')
    axs[1, 2].legend(loc="lower right", prop={'size': 6})
    axs[1, 2].set_ylabel("Delata3")

plt.subplots_adjust(top=0.957,
                    bottom=0.081,
                    left=0.131,
                    right=0.957,
                    hspace=0.235,
                    wspace=0.548)
# plt.savefig('fixed_seed_GPU_vs_CPU_tf_2_4_1_tf_2_5_1.eps', dpi=2000, bbox_inches="tight")

plt.show()