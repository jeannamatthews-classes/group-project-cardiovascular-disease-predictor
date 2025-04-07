function riskColor(riskLevel) {
    if(riskLevel === "low") {
        return "green";
    }
    else if(riskLevel === "moderate") {
        return "yellow";
    }
    else if(riskLevel === "high") {
        return "red";
    }
}

const DM_RISK = "low";
const HTN_RISK = "low";
const CAD_RISK = "moderate";
const CMP_RISK = "low";
const CKD_RISK = "low";

const leftDiv = document.createElement("div");
leftDiv.id = "leftDiv";
const rightDiv = document.createElement("div");
rightDiv.id = "rightDiv";

const DM_DESCRIPTION = document.createElement("p");
DM_DESCRIPTION.innerHTML = `Risk of DM : `;
const HTN_DESCRIPTION = document.createElement("p");
HTN_DESCRIPTION.innerHTML = `Risk of HTN: `;
const CAD_DESCRIPTION = document.createElement("p");
CAD_DESCRIPTION.innerHTML = `Risk of CAD: `;
const CMP_DESCRIPTION = document.createElement("p");
CMP_DESCRIPTION.innerHTML = `Risk of CMP: `;
const CKD_DESCRIPTION = document.createElement("p");
CKD_DESCRIPTION.innerHTML = `Risk of CKD: `;

const DM_RESULT = document.createElement("p");
DM_RESULT.innerHTML = `${DM_RISK}`;
DM_RESULT.style.color = riskColor(DM_RISK);
const HTN_RESULT = document.createElement("p");
HTN_RESULT.innerHTML = `${HTN_RISK}`;
HTN_RESULT.style.color = riskColor(HTN_RISK);
const CAD_RESULT = document.createElement("p");
CAD_RESULT.innerHTML = `${CAD_RISK}`;
CAD_RESULT.style.color = riskColor(CAD_RISK);
const CMP_RESULT = document.createElement("p");
CMP_RESULT.innerHTML = `${CMP_RISK}`;
CMP_RESULT.style.color = riskColor(CMP_RISK);
const CKD_RESULT = document.createElement("p");
CKD_RESULT.innerHTML = `${CKD_RISK}`;
CKD_RESULT.style.color = riskColor(CKD_RISK);

const container = document.getElementById("container");
container.appendChild(leftDiv);
container.appendChild(rightDiv);
leftDiv.appendChild(DM_DESCRIPTION);
leftDiv.appendChild(HTN_DESCRIPTION);
leftDiv.appendChild(CAD_DESCRIPTION);
leftDiv.appendChild(CMP_DESCRIPTION);
leftDiv.appendChild(CKD_DESCRIPTION);
rightDiv.appendChild(DM_RESULT);
rightDiv.appendChild(HTN_RESULT);
rightDiv.appendChild(CAD_RESULT);
rightDiv.appendChild(CMP_RESULT);
rightDiv.appendChild(CKD_RESULT);