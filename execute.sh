for name in  mushrooms
do
for population in 10 20 50 
do
for iteration_limit in 10 20 50 
do
for stop_criteria in 0 #E(0, 1, 2)
do
for probs_type in  0 #E(0, 1)
do
for crossover_type in  0 1 #E(0, 1, 2 , 3)
do
for crossover_rate in 0.1 0.5 # Pr~(0-1)
do
for mutation_type in  0 1 #E(0, 1)
do
for mutation_rate in  0 0.1 # Pr~(0-1)
do
for use_threads in  0  #0=False, 1=True
do
for cut_half_pop in  0   #0=False, 1=True
do
for replicate_best in  0 0.1   #Pr~(0-1)
do
 
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
done
done
done
done
done
done
done
done
done
done 

