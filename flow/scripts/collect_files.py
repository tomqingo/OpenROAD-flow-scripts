import os

# base_dir
base_dir = "/uac/gds/qluo22/disk/projects/OpenROAD-flow-scripts/flow"
object_dir = os.path.join(base_dir, "objects")
output_dir = os.path.join(base_dir, "data_openroad")

# output the directory
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# run the commands
def run(command):
    if os.system(command) is not 0:
        print(command)
        quit()

for impl in os.listdir(object_dir):
    # implementation directory
    impl_dir = os.path.join(object_dir, impl)
    # design
    for design in os.listdir(impl_dir):
        design_dir = os.path.join(impl_dir, design)
        # rtlmp_dir
        rtlmp_dir = os.path.join(design_dir, "base", "rtlmp")
        print(rtlmp_dir)

        # whether the rtlmp_dir exists
        if os.path.exists(rtlmp_dir):
            # blk_file
            blk_file = os.path.join(rtlmp_dir, "blk.csv")
            # net_file
            net_file = os.path.join(rtlmp_dir, "net.csv")
            # tml file
            tml_file = os.path.join(rtlmp_dir, "tml.csv")

            print(os.path.join(output_dir, impl + "_" + design + ".blk.csv"))

            if os.path.exists(blk_file):
                run("cp {} {}".format(blk_file, os.path.join(output_dir, impl + "_" + design + ".blk.csv")))
            
            if os.path.exists(net_file):
                run("cp {} {}".format(net_file, os.path.join(output_dir, impl + "_" + design + ".net.csv")))

            if os.path.exists(tml_file):
                run("cp {} {}".format(tml_file, os.path.join(output_dir, impl + "_" + design + ".tml.csv")))





