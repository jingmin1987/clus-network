# clus-network
A network visualization to show
* How SAS' Proc Varclus groups the existing variables 
* Where the new variables fit into the current structure

# Purpose
The idea behind this visualization is to explore new variables from LexisNexis to see if they can provide any additional information structure-wise (less correlated with existing structure). This information is then combined with IV or Gini statistics to filter the strong and less-correlated ones.

# Interactive Graph
In the following graph, each edge represents a correlation bound that is above 0.5 and each node is either a cluster component (big circle), or existing variables (small circle) or LexisNexis variables (x shape).

## Update on 3/1/2017
After rounds of exploration, it seems that LN variables are less correlated to the existing cluster structure and thus another Proc Varclus was performed on the LN variables alone. Proc score was used to reconstruct the cluster components of the existing structure so that LN variables could be re-assigned to existing structure if they appear closer to the existing one.

Please click on the following graph for interaction.

<div>
    <a href="https://plot.ly/~jingmin1987/12/?share_key=KyGESQQN55dw7kKkES7HHO" target="_blank" title="varclus_ln_med_all" style="display: block; text-align: center;"><img src="https://plot.ly/~jingmin1987/12.png?share_key=KyGESQQN55dw7kKkES7HHO" alt="varclus_ln_med_all" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="jingmin1987:12" sharekey-plotly="KyGESQQN55dw7kKkES7HHO" src="https://plot.ly/embed.js" async></script>
</div>

