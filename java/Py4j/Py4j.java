package Py4j;

import py4j.GatewayServer;
import Py4j.CommandAgent;
import negotiator.DeadlineType;

public class Py4j{
	private CommandAgent agent;
    public Py4j() {
    	agent = new CommandAgent();
    }

    public boolean setAgent(String xmlSettingFileName, String xmlFileName, int typeOfDeadline, int max_time, long seed, String agent_id, int agent_num){
    	boolean successToCreateFlag = false;
    	if(typeOfDeadline == 0)
    		successToCreateFlag = agent.createAgent(xmlSettingFileName, xmlFileName, DeadlineType.ROUND, max_time, seed, agent_id);
    	else if(typeOfDeadline == 1)
    		successToCreateFlag = agent.createAgent(xmlSettingFileName, xmlFileName, DeadlineType.TIME, max_time, seed, agent_id);
    	agent.informMessage(agent_num);
    	return successToCreateFlag;
    }
    
    public boolean receiveAction(String id, String typeOfAction, String bid){    	
    	//System.out.println("receive action");
    	//System.out.println(id+typeOfAction+bid);
    	return agent.receiveMessage(id, typeOfAction, bid);
    }
    //offer,endNegotiation,acceptのいずれかを返す
    public String sendAction(){
    	//System.out.println("send action");
    	String str = agent.chooseAction();
    	//System.out.println(str);
    	return str;
    }
    
    public String getName(){
    	return agent.getName();
    }

    public static void main(String[] args) {
    	int port_num = 25541;
        if(args.length > 0 && Integer.parseInt(args[0]) >= 25535)
        	port_num = Integer.parseInt(args[0]);
        GatewayServer gatewayServer = new GatewayServer(new Py4j(), port_num);
        gatewayServer.start();
        System.out.println("Gateway Server Started Port:"+port_num);
    }

}
