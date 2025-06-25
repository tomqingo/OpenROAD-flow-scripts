export RTLMP_READ=false
export RTLMP_CONTINUE=true

make

mkdir data_openroad
cp objects/nangate45/ariane133/base/rtlmp/blk.csv data_openroad/nangate45_ariane133.blk.csv
cp objects/nangate45/ariane133/base/rtlmp/net.csv data_openroad/nangate45_ariane133.net.csv
cp objects/nangate45/ariane133/base/rtlmp/tml.csv data_openroad/nangate45_ariane133.tml.csv
cp objects/nangate45/ariane133/base/rtlmp/fp.txt data_openroad/nangate45_ariane133.fp.txt

source ../FlexPlanner/script/test_2.sh

rm -f results/nangate45/ariane133/base/2_4_floorplan_macro.odb

export RTLMP_READ=true

make








