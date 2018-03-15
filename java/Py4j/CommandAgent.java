package Py4j;

import java.io.Serializable;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import negotiator.AgentID;
import negotiator.Bid;
import negotiator.Deadline;
import negotiator.DeadlineType;
import negotiator.Domain;
import negotiator.DomainImpl;
import negotiator.actions.Accept;
import negotiator.actions.Inform;
import negotiator.actions.Action;
import negotiator.actions.EndNegotiation;
import negotiator.actions.Offer;
import negotiator.issue.Issue;
import negotiator.issue.IssueDiscrete;
import negotiator.issue.Value;
import negotiator.issue.ValueDiscrete;
import negotiator.parties.AbstractNegotiationParty;
import negotiator.parties.NegotiationInfo;
import negotiator.persistent.DefaultPersistentDataContainer;
import negotiator.persistent.PersistentDataContainer;
import negotiator.persistent.PersistentDataType;
import negotiator.timeline.ContinuousTimeline;
import negotiator.timeline.DiscreteTimeline;
import negotiator.timeline.TimeLineInfo;
import negotiator.utility.AbstractUtilitySpace;
import negotiator.utility.AdditiveUtilitySpace;


// import AgentF.AgentF;
// import LinearAgent.LinearAgent;
// import BoulwareAgent.BoulwareAgent;
// import ConcederAgent.ConcederAgent;
// import YXAgent.YXAgent;
// import ParsCat.ParsCat;
// import Atlas3.Atlas3;
// import Caduceus2.Caduceus2;

public class CommandAgent {
	private AbstractNegotiationParty agent;
	private NegotiationInfo negotiationInfo;
    private Domain domain;
    private AbstractUtilitySpace utilSpace;
    private Deadline deadline;
    private TimeLineInfo timeline;
    private long randomSeed;
    private AgentID agentID;
    private PersistentDataContainer storage;
    private boolean isFirstTurn = true;
    private ArrayList<Issue> issues;
    private HashMap<Issue, HashMap<String, Value>> string2value = null;

	public CommandAgent() {
		// TODO Auto-generated constructor stub
	}
	public class Serialize implements Serializable{
	}
	public Boolean createNegotiationInfo(String setting_file_name, String file_name, DeadlineType tp, int max_time, long seed, String agent_id) {
		try {
			domain = new DomainImpl(setting_file_name);
			utilSpace = new AdditiveUtilitySpace(domain, file_name);
			deadline = new Deadline(max_time, tp);
			if(tp == DeadlineType.ROUND)
				timeline = new DiscreteTimeline(max_time);
			else if(tp == DeadlineType.TIME)
				timeline = new ContinuousTimeline(max_time);
			else
				return false;
			randomSeed = seed;
			agentID = new AgentID(agent_id);
			storage = new DefaultPersistentDataContainer(new Serialize(), PersistentDataType.DISABLED);

			negotiationInfo = new NegotiationInfo(utilSpace, deadline, timeline, randomSeed, agentID, storage);
		} catch (Exception e) {
			// TODO: handle exception
			System.out.println(e);
			return false;
		}
		return true;
	}
	public Boolean createAgent(String setting_file_name, String file_name, DeadlineType tp, int max_time, long seed, String agent_id) {
		if (createNegotiationInfo(setting_file_name, file_name, tp, max_time, seed, agent_id) == false)
			return false;
		isFirstTurn = true;
//		agent = new AgentF();
//		agent = new LinearAgent(); //25535
//		agent = new ConcederAgent(); //25536
//		agent = new BoulwareAgent(); //25537
//		agent = new YXAgent(); //25538
//		agent = new ParsCat(); //25539
		// agent = new Caduceus2(); //25541
		agent.init(negotiationInfo);
		makingString2Value();
		return true;
	}

	public void makingString2Value(){
		issues = (ArrayList<Issue>) utilSpace.getDomain().getIssues();
		string2value = new HashMap<Issue, HashMap<String, Value>> ();
		for(Issue issue:issues){
			string2value.put(issue, new HashMap<String, Value>()); // 論点行の初期化
			List<ValueDiscrete> values = ((IssueDiscrete)issue).getValues();
			for(Value value:values){ string2value.get(issue).put(value.toString(), value); } // 論点行の要素の初期化
    	}
		//System.out.println(string2value);
	}

	//agentにActionを起こさせ、それをPythonへ送る。
	public String chooseAction() {
		List<Class<? extends Action>> validActions = new ArrayList<Class<? extends Action>>();
		if(!isFirstTurn)
			validActions.add(Accept.class);
		validActions.add(EndNegotiation.class);
		validActions.add(Offer.class);
		negotiator.actions.Action action = agent.chooseAction(validActions);
		if(timeline instanceof DiscreteTimeline)
			((DiscreteTimeline) timeline).increment();
		return actionToString(action);
	}

	public String actionToString(Action action){
		String id = action.getAgent().getName();
		Bid bid = null;
		if(action instanceof Offer){
			bid = ((Offer) action).getBid();
			String bidString = bid.getValues().toString().replaceAll(" ", "");
			return id + ",Offer," + bidString.substring(1, bidString.length()-1);
		}
		else if(action instanceof EndNegotiation)
			return id + ",EndNegotiation";
		else if(action instanceof Accept)
			return id + ",Accept";
		return "fail to get action";
	}

	//pythonから受け取った情報を、agentに送る。
	public Boolean receiveMessage(String id, String typeOfAction, String bid_str){
		if(isFirstTurn)
			isFirstTurn = false;
		Bid bid = stringToBid(bid_str);
		AgentID agentID = new AgentID(id);
		Action act = null;
		if (typeOfAction.contains("Offer")){
			act = new Offer(agentID, bid);
		}
		else if(typeOfAction.contains("Accept")){
			act = new Accept(agentID, bid);
		}
		else if(typeOfAction.contains("EndNegotiation"))
			act = new EndNegotiation(agentID);
		agent.receiveMessage(agentID, act);
		return true;
	}
	public Bid stringToBid(String bid_str){
		Bid bid = utilSpace.getDomain().getRandomBid(new Random());
		if(bid_str.equals(""))
			return bid;
		String[] bid_strs = bid_str.split(",", 0);
		for(int i=0; i < issues.size(); i++)
			bid = bid.putValue(i+1, string2value.get(issues.get(i)).get(bid_strs[i]));
		return bid;
	}

	public void informMessage(int agent_num){
		Inform inform = new Inform(agentID, "NumberOfAgents", agent_num);
		agent.receiveMessage(agentID, inform);
	}
	public String getName(){
		return agent.getDescription();
	}


}
