#!/bin/bash

for name in glass #bands #flag  cellphone
do

for config in 4 4 4 4 #0 1 2 3 4 5 6 7 8 
do

population=50
iteration_limit=100
stop_criteria=1
probs_type=0
crossover_type=3
crossover_rate=0.8
mutation_type=0
mutation_rate=0.03
use_threads=0
cut_half_pop=0
replicate_best=0.1


if [ $config = '0' ];
then
    echo "Basic Configuration"
elif [ $config = '1' ];
then
    echo "Configuration 1"
    population=10
elif [ $config = '2' ];
then
    echo "Configuration 2"
    iteration_limit=200 
elif [ $config = '3' ];
then
    echo "Configuration 3"
    stop_criteria=0 
elif [ $config = '4' ];
then
    echo "Configuration 4"
    crossover_type=2 
elif [ $config = '5' ];
then
    echo "Configuration 5"
    crossover_rate=0.5 
elif [ $config = '6' ];
then
    echo "Configuration 6"
    mutation_type=1 
elif [ $config = '7' ];
then
    echo "Configuration 7"
    mutation_rate=0.15 
elif [ $config = '8' ];
then
    echo "Configuration 8"
    replicate_best=0 
fi


   python main.py \
    --dataset="./data/${name}.csv" \
    --population="${population}" \
    --iteration_limit="${iteration_limit}" \
    --stop_criteria="${stop_criteria}" \
    --probs_type="${probs_type}" \
    --crossover_type="${crossover_type}" \
    --crossover_rate="${crossover_rate}" \
    --mutation_type="${mutation_type}" \
    --mutation_rate="${mutation_rate}" \
    --use_threads="${use_threads}" \
    --cut_half_pop="${cut_half_pop}" \
    --replicate_best="${replicate_best}" 



done
done






# for population in 50
# do
# for iteration_limit in 100
# do
# for stop_criteria in 0 #E(0, 1, 2)
# do
# for probs_type in  0 #E(0, 1)
# do
# for crossover_type in  3 #E(0, 1, 2 , 3)
# do
# for crossover_rate in 0.8 # Pr~(0-1)
# do
# for mutation_type in  0  #E(0, 1)
# do
# for mutation_rate in  0.03 # Pr~(0-1)
# do
# for use_threads in  0  #0=False, 1=True
# do
# for cut_half_pop in  0   #0=False, 1=True
# do
# for replicate_best in  0.1   #Pr~(0-1)
# do


# done
# done
# done
# done
# done
# done
# done
# done
# done
# done
# done


